import { open, shot, openWorkflow } from './lib.mjs';
import { withApi } from './api.mjs';
let W = {}; await withApi(async (api) => { const r = await api('GET', '/workflows'); for (const w of r.data) W[w.name] = w.id; });
const { browser, page } = await open();
for (const [name, file] of [['Error logger', 'kit-canvas-4'], ['Capture', 'kit-canvas-1'], ['Notion button', 'kit-canvas-2'], ['Daily briefing', 'kit-canvas-3'], ['MCP', 'kit-canvas-5']]) {
  const id = Object.entries(W).find(([n]) => n.includes(name))[1];
  await openWorkflow(page, id);
  const x = page.getByText('Production Checklist'); if (await x.count()) { const b = await x.boundingBox(); await page.mouse.click(b.x + 320, b.y + 9); }
  await page.locator('[data-test-id="zoom-to-fit"]').click(); await page.waitForTimeout(700); await page.mouse.move(1300, 800);
  await shot(page, file);
}
await browser.close();
