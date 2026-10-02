import { open, shot, BASE, openWorkflow } from './lib.mjs';
import { withApi } from './api.mjs';
import { execSync } from 'child_process';
let W = {}; await withApi(async (api) => { const r = await api('GET', '/workflows'); for (const w of r.data) W[w.name] = w.id; });
const id = (s) => Object.entries(W).find(([n]) => n.includes(s))[1];
const { browser, ctx, page } = await open();
const ndv = page.locator('[data-test-id="ndv"]');
const away = () => page.mouse.move(1300, 650);
const openNode = async (name) => { await page.locator(`[data-test-id="canvas-node"][data-node-name="${name}"]`).first().dblclick({ force: true }); await page.waitForTimeout(1500); };
const closeNdv = async () => { const b = page.locator('[data-test-id="ndv-close-button"]').first(); if (await b.isVisible().catch(() => false)) { await b.click(); await page.waitForTimeout(600); } };

// before publishing it: the error logger shows a ⚠️ "Not published" in other workflows' settings
await openWorkflow(page, id('Capture'));
await page.locator('[data-test-id="workflow-menu"]').click(); await page.waitForTimeout(600);
await page.getByText('Settings', { exact: true }).last().click(); await page.waitForTimeout(1500);
await page.locator('[role="dialog"]').last().locator('.el-select').nth(1).click(); await page.waitForTimeout(800);
await page.locator('li[role="option"]').filter({ hasText: 'Error logger' }).locator('svg, [class*="icon"]').last().hover().catch(() => {});
await page.waitForTimeout(800); await shot(page, 'kit-26-error-workflow-pick');
await page.keyboard.press('Escape'); await page.keyboard.press('Escape'); await page.waitForTimeout(600);

// publish the error logger first
await openWorkflow(page, id('Error logger'));
await away(); await shot(page, 'kit-13-error-logger-canvas');
if (!(await page.getByText('Published', { exact: true }).count())) {
await page.locator('[data-test-id="workflow-open-publish-modal-button"]').click(); await page.waitForTimeout(1200);
await page.locator('[role="dialog"]').last().getByRole('button', { name: 'Publish' }).click(); await page.waitForTimeout(2500); }
const got = page.getByRole('button', { name: 'Got it' }); if (await got.count()) await got.click();
await page.waitForTimeout(800); await away(); await shot(page, 'kit-14-error-logger-published');

await openWorkflow(page, id('Capture'));
// error workflow setting
await page.locator('[data-test-id="workflow-menu"]').click(); await page.waitForTimeout(600);
await page.getByText('Settings', { exact: true }).last().click(); await page.waitForTimeout(1500);
const dlg = page.locator('[role="dialog"]').last();
await dlg.locator('.el-select').nth(1).click(); await page.waitForTimeout(800);
await page.getByRole('option', { name: /Error logger/ }).first().click().catch(e => console.log('opt', e.message)); await page.waitForTimeout(600);
await away(); await shot(page, 'kit-27-error-workflow-set');
await dlg.getByRole('button', { name: 'Save' }).click().catch(e => console.log('save', e.message)); await page.waitForTimeout(1500);

// connect Claude
await openNode('Claude (fast)');
const conn = ndv.getByText('Connect to Anthropic');
if (await conn.count()) {
  await conn.click(); await page.waitForTimeout(1200);
  const m = page.locator('[data-test-id="editCredential-modal"]');
  await m.locator('[data-test-id="parameter-input-apiKey"] input').fill('sk-ant-api03-paste-your-own-key-here');
  await m.locator('[data-test-id="parameter-input-url"] input').fill('http://127.0.0.1:8788');
  await m.locator('[data-test-id="credential-save-button"]').click(); await page.waitForTimeout(2000);
  await m.locator('button:has(svg[data-icon="x"]), .el-dialog__headerbtn').first().click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(600);
}
await away(); await shot(page, 'kit-28-claude-connected');
await closeNdv();
// paste the database link
await openNode('Create Inbox row');
await away(); await shot(page, 'kit-29-database-link');
await closeNdv();

// test run with curl
await page.locator('[data-test-id="execute-workflow-button"]').click(); await page.waitForTimeout(2000);
await away(); await shot(page, 'kit-30-listening');
const out = execSync(`curl -s -X POST http://localhost:5678/webhook-test/capture -H "Content-Type: application/json" -H "X-Webhook-Secret: a-long-random-secret-from-your-password-manager" -d '{"text": "remember to renew the car insurance before the 20th, check if bundling with home is cheaper", "source": "Phone"}'`).toString();
console.log('CURL:', out.slice(0, 300));
await page.waitForTimeout(6000); await away();
await shot(page, 'kit-31-test-run');
await openNode('Parse and validate'); await away();
await shot(page, 'kit-32-parsed-output');
await closeNdv();
await openNode('Create Inbox row'); await away();
await shot(page, 'kit-33-notion-error');
console.log('ERR:', (await ndv.innerText()).slice(0, 1500));
await browser.close();
