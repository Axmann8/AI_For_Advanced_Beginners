// Builds "Quick note → AI summary" in a fresh n8n, the way a reader would, and captures each step.
import { open, shot, BASE, plusAfter, plusBelow, drag } from './lib.mjs';
const P = 'first-';
const { browser, ctx, page } = await open();
const ndv = page.locator('[data-test-id="ndv"]');
const away = () => page.mouse.move(1300, 650);

// 1 · Overview → Build a workflow
await page.goto(BASE + '/home/workflows'); await page.getByText('Build a workflow').waitFor(); await page.waitForTimeout(800);
await shot(page, P + '01-overview');
await page.getByText('Build a workflow').click(); await page.getByText('Add first step').waitFor(); await page.waitForTimeout(1200);
// rename
await page.locator('[data-test-id="workflow-name-input"]').click(); await page.waitForTimeout(300);
await page.keyboard.press('Control+a'); await page.keyboard.type('Quick note → AI summary'); await page.keyboard.press('Enter');
await page.waitForTimeout(800); await away();
await shot(page, P + '02-empty-canvas');

// 2 · Trigger
{ const b = await page.getByText('Add first step').boundingBox(); await page.mouse.click(b.x + b.width / 2, b.y - 70); } await page.waitForTimeout(1200);
await shot(page, P + '03-trigger-panel');
await page.getByText('On form submission').click(); await page.waitForTimeout(1800);
await ndv.getByPlaceholder('e.g. Contact us').fill('Quick note');
await ndv.getByPlaceholder("e.g. We'll get back to you soon").fill('Jot down anything. AI will sort it for you.');
await ndv.getByText('Add Form Element').click(); await page.waitForTimeout(800);
await ndv.getByPlaceholder('e.g. What is your name?').fill('Your note');
await ndv.locator('[data-test-id="parameter-input-fieldType"]').click(); await page.waitForTimeout(500);
await page.getByRole('option', { name: 'Textarea' }).first().click(); await page.waitForTimeout(500);
await away(); await shot(page, P + '04-form-settings');
let [popup] = await Promise.all([ctx.waitForEvent('page'), ndv.locator('[data-test-id="node-execute-button"]').click()]);
await popup.waitForLoadState(); await popup.setViewportSize({ width: 900, height: 560 }); await popup.waitForTimeout(1500);
await popup.locator('textarea').first().fill('The landlord needs to know by tonight if Thursday 10am works for the boiler repair.');
await popup.screenshot({ path: new URL('./raw/' + P + '05-test-form.png', import.meta.url).pathname }); console.log('📸 05');
await popup.getByRole('button', { name: /Submit/ }).click(); await popup.waitForTimeout(1200); await popup.close();
await page.bringToFront(); await page.waitForTimeout(2000); await away();
await shot(page, P + '06-trigger-output');
await page.locator('[data-test-id="ndv-close-button"]').click(); await page.waitForTimeout(800);

// 3 · AI step
await plusAfter(page, 'On form submission'); await page.waitForTimeout(1200);
await shot(page, P + '07-next-step');
await page.keyboard.type('Basic LLM', { delay: 40 }); await page.waitForTimeout(900);
await page.getByText('Basic LLM Chain').first().click(); await page.waitForTimeout(1800);
await ndv.locator('[data-test-id="parameter-input-promptType"]').click(); await page.waitForTimeout(400);
await page.getByRole('option', { name: /Define below/ }).click(); await page.waitForTimeout(700);
const field = ndv.locator('[data-test-id="parameter-input-text"]');
await field.click(); await page.waitForTimeout(300);
await page.keyboard.type('Summarize this note in one short sentence, then say if it is urgent (Yes or No).', { delay: 3 });
await page.keyboard.press('Enter'); await page.keyboard.press('Enter'); await page.keyboard.type('Note: ', { delay: 3 });
const drop = await drag(page, ndv.getByText('Your note', { exact: true }).first(), field, 0.6, 0.85);
await shot(page, P + '08-drag-field', { wait: 200 });
await drop(); await page.waitForTimeout(900); await away();
await shot(page, P + '09-prompt-done', { keepToast: true });

// 4 · Model + credential
await page.locator('[data-test-id="ndv-close-button"]').first().click(); await page.waitForTimeout(800); await away();
await shot(page, P + '09b-needs-model');
await plusBelow(page, 'Basic LLM Chain'); await page.waitForTimeout(1200);
await page.keyboard.type('Anthropic', { delay: 40 }); await page.waitForTimeout(800);
await shot(page, P + '10-model-picker');
await page.getByText('Anthropic Chat Model').first().click(); await page.waitForTimeout(1800);
await page.getByText('Connect to Anthropic').click(); await page.waitForTimeout(1500);
const modal = page.locator('[data-test-id="editCredential-modal"]');
await modal.locator('[data-test-id="parameter-input-apiKey"] input').fill('sk-ant-api03-paste-your-own-key-here');
await away(); await shot(page, P + '11-credential');
await modal.locator('[data-test-id="parameter-input-url"] input').fill('http://127.0.0.1:8788');
await modal.locator('[data-test-id="credential-save-button"]').click(); await page.waitForTimeout(2500);
await modal.locator('.el-dialog__headerbtn, button[aria-label="Close"], [data-test-id="close-button"]').first().click().catch(e => console.log('noclose', e.message));
await page.waitForTimeout(800);
await away(); await shot(page, P + '12-model-ready');
await page.locator('[data-test-id="ndv-close-button"]').first().click(); await page.waitForTimeout(800);
await page.keyboard.press('Shift+1'); await page.waitForTimeout(400);
await shot(page, P + '13-canvas-two');

// 5 · Form ending
await plusAfter(page, 'Basic LLM Chain'); await page.waitForTimeout(1200);
await page.keyboard.type('n8n Form', { delay: 40 }); await page.waitForTimeout(800);
await page.getByText('n8n Form', { exact: true }).first().click(); await page.waitForTimeout(1000);
await page.getByText('Form Ending', { exact: true }).first().click(); await page.waitForTimeout(1800);
await ndv.locator('[data-test-id="parameter-input-completionTitle"] input').fill('Got it! Here is your AI summary');
const msg = ndv.locator('[data-test-id="parameter-item"]').filter({ hasText: 'Completion Message' }).first();
await msg.hover(); await msg.locator('[data-test-id="radio-button-expression"]').click(); await page.waitForTimeout(500);
await msg.locator('.cm-content').first().click(); await page.keyboard.type('{{ $json.text', { delay: 20 }); await page.waitForTimeout(500);
await away(); await shot(page, P + '14-form-ending');
console.log('msg=', await msg.locator('.cm-content').first().innerText());
await page.locator('[data-test-id="ndv-close-button"]').first().click(); await page.waitForTimeout(800);
await page.locator('[data-test-id="zoom-to-fit"]').click(); await page.waitForTimeout(600); await away();
await shot(page, P + '15-canvas-complete');

// 6 · Run it end to end
[popup] = await Promise.all([ctx.waitForEvent('page'), page.locator('[data-test-id="execute-workflow-button"]').click()]);
await popup.waitForLoadState(); await popup.setViewportSize({ width: 900, height: 560 }); await popup.waitForTimeout(1500);
await popup.locator('textarea').first().fill('The landlord needs to know by tonight if Thursday 10am works for the boiler repair.');
await popup.getByRole('button', { name: /Submit/ }).click(); await popup.waitForTimeout(5000);
await popup.screenshot({ path: new URL('./raw/' + P + '16-form-result.png', import.meta.url).pathname }); console.log('📸 16');
await popup.close(); await page.bringToFront(); await page.waitForTimeout(1500); await away();
await shot(page, P + '17-canvas-success');
await page.locator('[data-test-id="canvas-node"]').filter({ hasText: 'Basic LLM Chain' }).first().dblclick({ force: true }); await page.waitForTimeout(1500);
await away(); await shot(page, P + '18-chain-output');
await page.locator('[data-test-id="ndv-close-button"]').first().click(); await page.waitForTimeout(800);

// 7 · Publish and check executions
await page.locator('[data-test-id="workflow-open-publish-modal-button"]').click(); await page.waitForTimeout(1500);
await away(); await shot(page, P + '19-publish');
await page.locator('[role="dialog"]').last().getByRole('button', { name: 'Publish' }).click(); await page.waitForTimeout(2500);
await away(); await shot(page, P + '20-published');
await page.getByRole('button', { name: 'Got it' }).click(); await page.waitForTimeout(1500);
const checklist = page.getByText('Production Checklist');
if (await checklist.count()) {
  await away(); await shot(page, P + '20a-production-checklist');
  const box = await checklist.boundingBox(); await page.mouse.click(box.x + 320, box.y + 9); await page.waitForTimeout(600);
}
await page.locator('[data-test-id="canvas-node"]').filter({ hasText: 'On form submission' }).first().dblclick({ force: true }); await page.waitForTimeout(1500);
await ndv.locator('[data-test-id="radio-button-production"]').click(); await page.waitForTimeout(600);
await away(); await shot(page, P + '20b-production-url');
const prodUrl = (await ndv.innerText()).match(/http:\/\/localhost:5678\/form\/[\w-]+/)[0]; console.log(prodUrl);
await page.locator('[data-test-id="ndv-close-button"]').first().click(); await page.waitForTimeout(600);
const live = await ctx.newPage(); await live.setViewportSize({ width: 900, height: 560 });
await live.goto(prodUrl); await live.waitForTimeout(1500);
await live.locator('textarea').first().fill('Reminder: renew the car insurance before the 20th, and check whether bundling with home insurance is cheaper.');
await live.screenshot({ path: new URL('./raw/' + P + '20c-live-form.png', import.meta.url).pathname }); console.log('📸 20c');
await live.getByRole('button', { name: /Submit/ }).click(); await live.waitForTimeout(5000);
await live.screenshot({ path: new URL('./raw/' + P + '20d-live-result.png', import.meta.url).pathname }); console.log('📸 20d');
await live.close(); await page.bringToFront();
await page.locator('[data-test-id="radio-button-executions"]').click(); await page.waitForTimeout(2500);
await away(); await shot(page, P + '21-executions');
await page.goto(BASE + '/home/workflows'); await page.waitForTimeout(2500); await away();
await shot(page, P + '22-workflow-list');
await browser.close();
