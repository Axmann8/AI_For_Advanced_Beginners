import { open, shot, BASE, openWorkflow } from './lib.mjs';
import { withApi } from './api.mjs';
let W = {}; await withApi(async (api) => { const r = await api('GET', '/workflows'); for (const w of r.data) W[w.name] = w.id; });
const id = (s) => Object.entries(W).find(([n]) => n.includes(s))[1];
const { browser, ctx, page } = await open();
const ndv = page.locator('[data-test-id="ndv"]');
const away = () => page.mouse.move(1300, 650);
const openNode = async (name) => { await page.locator(`[data-test-id="canvas-node"][data-node-name="${name}"]`).first().dblclick({ force: true }); await page.waitForTimeout(1500); };
const closeNdv = async () => { await page.locator('[data-test-id="ndv-close-button"]').first().click(); await page.waitForTimeout(600); };

// Import submenu
await page.goto(BASE + '/workflow/new'); await page.getByText('Add first step').waitFor(); await page.waitForTimeout(1000);
await page.locator('[data-test-id="workflow-menu"]').click(); await page.waitForTimeout(600);
await page.getByText('Import', { exact: true }).hover(); await page.waitForTimeout(800);
await shot(page, 'kit-02-import-submenu');
await page.keyboard.press('Escape');

// Error logger: Notion credential
await openWorkflow(page, id('Error logger'));
await openNode('Log to Notion'); await away();
await shot(page, 'kit-10-notion-node-nocred');
await page.getByText('Connect to Notion').click(); await page.waitForTimeout(1500);
const modal = page.locator('[data-test-id="editCredential-modal"]');
console.log('MODAL:', (await modal.innerText()).slice(0, 600));
await modal.locator('[data-test-id="parameter-input-apiKey"] input').fill('ntn_paste-your-internal-integration-secret');
await away(); await shot(page, 'kit-11-notion-credential');
await modal.locator('[data-test-id="credential-save-button"]').click(); await page.waitForTimeout(4000);
await away(); await shot(page, 'kit-12-notion-credential-saved');
console.log('AFTER:', (await modal.innerText()).slice(0, 600));
await browser.close();
