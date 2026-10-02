// Calls n8n's internal REST API from inside the logged-in browser (same cookies + browser-id header).
import { open, BASE } from './lib.mjs';
export async function withApi(fn) {
  const { browser, ctx, page } = await open();
  await page.goto(BASE + '/home/workflows'); await page.waitForTimeout(1500);
  const api = async (method, path, body) => page.evaluate(async ([method, path, body]) => {
    const bid = localStorage.getItem('n8n-browserId');
    const r = await fetch('/rest' + path, { method, headers: { 'content-type': 'application/json', 'browser-id': bid },
      body: body ? JSON.stringify(body) : undefined });
    const t = await r.text(); try { return { status: r.status, ...JSON.parse(t) }; } catch { return { status: r.status, text: t }; }
  }, [method, path, body]);
  try { return await fn(api, page); } finally { await browser.close(); }
}
