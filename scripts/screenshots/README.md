# 📸 Screenshot scripts

The n8n screenshots in the manual (`manual/assets/screenshots/n8n/`) are **real captures of a fresh n8n install**, made
by these scripts with [Playwright](https://playwright.dev). They click through the same steps a reader follows, so when
n8n changes its interface you can re-run them and the manual's pictures update in minutes.

The AI replies in the screenshots come from `mock_anthropic.py`, a tiny stand-in for the Anthropic API that returns
sample answers. That keeps captures free and repeatable; nothing else is mocked.

## Run them

```bash
# 1. A brand-new n8n (Node.js 24+), in a throwaway folder
N8N_USER_FOLDER=/tmp/n8n-shots N8N_DIAGNOSTICS_ENABLED=false N8N_PERSONALIZATION_ENABLED=false \
  GENERIC_TIMEZONE=Europe/London npx n8n@2.41.6 start &

# 2. The sample-answer AI on port 8788
python3 mock_anthropic.py 8788 &

# 3. Playwright (point PLAYWRIGHT_MODULE / CHROMIUM_PATH at an existing install if you have one)
npm install playwright && npx playwright install chromium

# 4. Capture, in this order
node setup_owner.mjs                       # owner account (also saves the login)
node cleanup.mjs && node first_workflow.mjs    # chapter 47: the first AI workflow, step by step
node cleanup.mjs && node kit_import.mjs    # Part XIV starter kit: import all five workflows
node kit_details.mjs && node kit_details2.mjs  # credentials, webhook, Notion node, settings
node kit_prep.mjs && node kit_run.mjs      # sample database links, error logger, test run
node kit_assign.mjs && node kit_canvases.mjs && node kit_more.mjs  # connected canvases and details

# 5. Crop and compress into the manual
pip install pillow && python3 optimize.py
```

`optimize.py` maps each raw capture to its final file name and crop, then reduces it to a 256-colour PNG (about 25 KB
each). Raw captures land in `raw/`, which isn't committed.
