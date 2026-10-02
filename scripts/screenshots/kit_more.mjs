import { open, shot, BASE, openWorkflow } from './lib.mjs';
import { withApi } from './api.mjs';
let W = {}; await withApi(async (api) => { const r = await api('GET', '/workflows'); for (const w of r.data) W[w.name] = w.id; });
const id = (s) => (Object.entries(W).find(([n]) => n.includes(s)) || [])[1];
const { browser, ctx, page } = await open();
const ndv = page.locator('[data-test-id="ndv"]');
const away = () => page.mouse.move(1300, 650);
const openNode = async (name) => { await page.locator(`[data-test-id="canvas-node"][data-node-name="${name}"]`).first().dblclick({ force: true }); await page.waitForTimeout(1500); };
const closeNdv = async () => { const b = page.locator('[data-test-id="ndv-close-button"]').first(); if (await b.isVisible().catch(() => false)) { await b.click(); await page.waitForTimeout(600); } };

await openWorkflow(page, id('Notion button'));
await away(); await shot(page, 'kit-40-button-canvas');
await openNode('Notion button webhook'); await away(); await shot(page, 'kit-41-button-webhook'); await closeNdv();

await openWorkflow(page, id('Daily briefing'));
await away(); await shot(page, 'kit-50-briefing-canvas');
await openNode('Every morning at 7'); await away(); await shot(page, 'kit-51-schedule'); await closeNdv();
await openNode('Open tasks due soon'); await away(); await shot(page, 'kit-52-notion-filter');
await ndv.locator('[data-test-id="ndv"] .el-scrollbar, [data-test-id="node-parameters"]').first().evaluate(e => e.scrollTop = 400).catch(() => {});
await page.mouse.move(720, 500); await page.mouse.wheel(0, 500); await page.waitForTimeout(500); await away();
await shot(page, 'kit-53-notion-filter-conditions'); await closeNdv();

await openWorkflow(page, id('MCP'));
await away(); await shot(page, 'kit-60-mcp-canvas');
await openNode('MCP Server Trigger'); await away(); await shot(page, 'kit-61-mcp-trigger');
console.log((await ndv.innerText()).slice(0, 600)); await closeNdv();
await openNode('find_tasks'); await away(); await shot(page, 'kit-62-mcp-tool');
await page.goto(BASE + '/settings/mcp'); await page.waitForTimeout(2000); await shot(page, 'mcp-instance-settings');
await browser.close();
