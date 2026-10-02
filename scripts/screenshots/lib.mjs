// Playwright is loaded from PLAYWRIGHT_MODULE (a path to playwright's index.mjs) or the normal 'playwright' package.
const { chromium } = await import(process.env.PLAYWRIGHT_MODULE || 'playwright');
import fs from 'fs';
export const BASE = process.env.N8N_URL || 'http://localhost:5678';
export const RAW = new URL('./raw/', import.meta.url).pathname;
export const STATE = new URL('./state.json', import.meta.url).pathname;
export async function open({ scale = 1, auth = true, w = 1440, h = 900 } = {}) {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: scale,
    storageState: auth && fs.existsSync(STATE) ? STATE : undefined, locale: 'en-US', timezoneId: 'Europe/London' });
  const page = await ctx.newPage();
  page.setDefaultTimeout(15000);
  return { browser, ctx, page };
}
export async function shot(page, name, opts = {}) {
  if (!opts.keepToast) {
    for (const b of await page.locator('.el-notification .el-notification__closeBtn').all()) if (await b.isVisible()) await b.click({ timeout: 1000 }).catch(() => {});
  }
  await page.waitForTimeout(opts.wait ?? 600);
  const path = RAW + name + '.png';
  if (opts.el) await page.locator(opts.el).first().screenshot({ path });
  else await page.screenshot({ path, clip: opts.clip, fullPage: false });
  console.log('📸', name);
}
export async function plusAfter(page, nodeName) {
  const node = page.locator('[data-test-id="canvas-node"]').filter({ hasText: nodeName }).first();
  await node.hover(); await page.waitForTimeout(300);
  const b = await node.boundingBox();
  const plus = page.locator('[data-test-id="canvas-handle-plus"]');
  const n = await plus.count();
  for (let i = 0; i < n; i++) {
    const pb = await plus.nth(i).boundingBox();
    if (pb && Math.abs(pb.y + pb.height / 2 - (b.y + b.height / 2)) < 40 && pb.x > b.x) { await plus.nth(i).click(); return; }
  }
  await page.mouse.click(b.x + b.width + 100, b.y + b.height / 2);
}
export async function openWorkflow(page, id) {
  await page.goto(BASE + '/workflow/' + id);
  await page.locator('[data-test-id="canvas-node"]').first().waitFor(); await page.waitForTimeout(1500);
  const edit = page.getByText('Edit here');
  if (await edit.count()) { await edit.first().click(); await page.waitForTimeout(1000); }
}
export async function drag(page, from, to, dx = 0.5, dy = 0.7) {
  const a = await from.boundingBox(), b = await to.boundingBox();
  await page.mouse.move(a.x + a.width / 2, a.y + a.height / 2); await page.mouse.down();
  for (let i = 1; i <= 15; i++) { await page.mouse.move(a.x + (b.x + b.width * dx - a.x) * i / 15, a.y + (b.y + b.height * dy - a.y) * i / 15); await page.waitForTimeout(30); }
  await page.waitForTimeout(400); return async () => { await page.mouse.up(); };
}

export async function plusBelow(page, nodeName) {
  const node = page.locator('[data-test-id="canvas-node"]').filter({ hasText: nodeName }).first();
  const b = await node.boundingBox();
  const plus = page.locator('[data-test-id="canvas-handle-plus"]');
  for (let i = 0; i < await plus.count(); i++) {
    const pb = await plus.nth(i).boundingBox();
    if (pb && pb.y > b.y + b.height && pb.x > b.x - 20 && pb.x < b.x + b.width) { await plus.nth(i).click(); return; }
  }
  throw new Error('no plus below ' + nodeName);
}
