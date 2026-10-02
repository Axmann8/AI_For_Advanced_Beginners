import { open, shot, BASE } from './lib.mjs';
const KIT = new URL('../../examples/n8n-notion/', import.meta.url).pathname;
const files = ['4-error-logger.json', '1-capture-to-inbox.json', '2-process-with-ai-button.json', '3-daily-briefing.json', '5-notion-tools-mcp-server.json'];
const { browser, ctx, page } = await open();
const away = () => page.mouse.move(1300, 650);
const ids = {};
for (const [i, f] of files.entries()) {
  await page.goto(BASE + '/workflow/new'); await page.getByText('Add first step').waitFor(); await page.waitForTimeout(1200);
  if (i === 0) {
    await page.locator('[data-test-id="workflow-menu"]').click(); await page.waitForTimeout(800);
    await shot(page, 'kit-01-import-menu');
    await page.keyboard.press('Escape'); await page.waitForTimeout(300);
  }
  await page.locator('[data-test-id="workflow-import-input"]').setInputFiles(KIT + f); await page.waitForTimeout(2500);
  await page.locator('[data-test-id="zoom-to-fit"]').click().catch(() => {}); await page.waitForTimeout(800);
  await page.keyboard.press('Control+s'); await page.waitForTimeout(1500); await away();
  ids[f] = page.url().split('/workflow/')[1]?.split('?')[0];
  await shot(page, 'kit-canvas-' + f.split('-')[0]);
}
console.log(JSON.stringify(ids));
await browser.close();
