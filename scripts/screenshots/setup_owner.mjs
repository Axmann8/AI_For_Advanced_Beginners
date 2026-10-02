// Step 0: create the owner account on a brand-new n8n and save the login for the other scripts.
import { open, shot, BASE, STATE } from './lib.mjs';
const { browser, ctx, page } = await open({ auth: false });
await page.goto(BASE + '/setup'); await page.waitForTimeout(2500);  // a fresh n8n opens the owner setup form
await page.getByLabel('Email').fill('you@example.com');
await page.getByLabel('First Name').fill('Alex');
await page.getByLabel('Last Name').fill('Rivera');
await page.getByLabel('Password').fill('Sample-Passw0rd');
await shot(page, 'setup-owner', { clip: { x: 520, y: 20, width: 400, height: 660 } });
await page.getByRole('button', { name: 'Next' }).click();
await page.waitForTimeout(4000);
console.log(page.url());
await shot(page, 'after-setup');
await ctx.storageState({ path: STATE });
await browser.close();
