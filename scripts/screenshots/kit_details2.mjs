import { open, shot, BASE, openWorkflow } from './lib.mjs';
import { withApi } from './api.mjs';
let W = {}; await withApi(async (api) => { const r = await api('GET', '/workflows'); for (const w of r.data) W[w.name] = w.id; });
const id = (s) => Object.entries(W).find(([n]) => n.includes(s))[1];
const { browser, ctx, page } = await open();
const ndv = page.locator('[data-test-id="ndv"]');
const away = () => page.mouse.move(1300, 650);
const openNode = async (name) => { await page.locator(`[data-test-id="canvas-node"][data-node-name="${name}"]`).first().dblclick({ force: true }); await page.waitForTimeout(1500); };
const closeNdv = async () => { const b = page.locator('[data-test-id="ndv-close-button"]').first(); if (await b.isVisible().catch(() => false)) { await b.click(); await page.waitForTimeout(600); } };

await openWorkflow(page, id('Capture'));
await openNode('Capture webhook'); await away();
await shot(page, 'kit-20-webhook-node');
console.log('WEBHOOK:', (await ndv.innerText()).slice(0, 900));
const credBtn = ndv.getByText(/Connect to|Set up credential|Create new credential/).first();
console.log('cred btn count', await credBtn.count());
if (await credBtn.count()) {
  await credBtn.click(); await page.waitForTimeout(1500);
  const modal = page.locator('[data-test-id="editCredential-modal"]');
  console.log('HDR MODAL:', (await modal.innerText()).slice(0, 500));
  await modal.locator('[data-test-id="parameter-input-name"] input').fill('X-Webhook-Secret');
  await modal.locator('[data-test-id="parameter-input-value"] input').fill('a-long-random-secret-from-your-password-manager');
  await away(); await shot(page, 'kit-21-header-auth-credential');
  await modal.locator('[data-test-id="credential-save-button"]').click(); await page.waitForTimeout(2000);
  await modal.locator('button:has(svg[data-icon="x"]), .el-dialog__headerbtn').first().click({ timeout: 3000 }).catch(e => console.log('noclose'));
  await page.waitForTimeout(800);
}
await away(); await shot(page, 'kit-22-webhook-ready');
await closeNdv();
await openNode('Create Inbox row'); await away();
await shot(page, 'kit-23-notion-create-inbox');
await closeNdv();
await openNode('Parse and validate'); await away();
await shot(page, 'kit-24-code-node');
await closeNdv();
// workflow settings → error workflow
await page.locator('[data-test-id="workflow-menu"]').click(); await page.waitForTimeout(600);
await page.getByText('Settings', { exact: true }).last().click(); await page.waitForTimeout(1500);
await away(); await shot(page, 'kit-25-workflow-settings');
console.log('SETTINGS:', (await page.locator('[role="dialog"]').last().innerText()).slice(0, 800));
await browser.close();
