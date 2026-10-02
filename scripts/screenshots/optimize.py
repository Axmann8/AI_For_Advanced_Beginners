import os
import sys

from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "../../manual/assets/screenshots/n8n/")
os.chdir(HERE)
NDV = (24, 24, 1416, 876)          # the node panel, without the dimmed canvas around it
FULL = None
M = {  # raw name: (output name, crop)
 "setup-owner": ("setup-owner-account", FULL),
 "first-01-overview": ("overview-first-run", (0, 0, 1440, 640)),
 "first-02-empty-canvas": ("empty-canvas", (0, 0, 1440, 600)),
 "first-03-trigger-panel": ("trigger-panel", FULL),
 "first-04-form-settings": ("form-trigger-settings", NDV),
 "first-05-test-form": ("test-form", (0, 0, 900, 440)),
 "first-06-trigger-output": ("form-trigger-output", NDV),
 "first-07-next-step": ("next-step-panel", FULL),
 "first-08-drag-field": ("drag-a-field", NDV),
 "first-09-prompt-done": ("prompt-mapped", NDV),
 "first-09b-needs-model": ("chain-needs-model", (420, 0, 1440, 640)),
 "first-10-model-picker": ("model-picker", FULL),
 "first-11-credential": ("anthropic-credential", (216, 90, 1224, 700)),
 "first-12-model-ready": ("anthropic-model-ready", NDV),
 "first-14-form-ending": ("form-ending", NDV),
 "first-15-canvas-complete": ("canvas-complete", (200, 0, 1440, 700)),
 "first-16-form-result": ("form-result-test", (0, 0, 900, 300)),
 "first-17-canvas-success": ("canvas-success", (200, 0, 1440, 700)),
 "first-18-chain-output": ("chain-output", NDV),
 "first-19-publish": ("publish-dialog", (440, 230, 1000, 670)),
 "first-20a-production-checklist": ("production-checklist", (200, 0, 1440, 700)),
 "first-20b-production-url": ("production-url", NDV),
 "first-20c-live-form": ("live-form", (0, 0, 900, 440)),
 "first-20d-live-result": ("live-result", (0, 0, 900, 300)),
 "first-21-executions": ("executions-list", FULL),
 "mcp-instance-settings": ("instance-level-mcp", (0, 0, 1440, 520)),
 "kit-02-import-submenu": ("import-menu", (200, 0, 1000, 480)),
 "kit-canvas-1": ("kit-1-capture", (200, 0, 1440, 680)),
 "kit-canvas-2": ("kit-2-button", (200, 0, 1440, 680)),
 "kit-canvas-3": ("kit-3-briefing", (200, 0, 1440, 700)),
 "kit-canvas-4": ("kit-4-error-logger", (200, 0, 1440, 640)),
 "kit-canvas-5": ("kit-5-mcp", (200, 0, 1440, 720)),
 "kit-10-notion-node-nocred": ("notion-node-before-setup", NDV),
 "kit-11-notion-credential": ("notion-credential", (216, 90, 1224, 700)),
 "kit-12-notion-credential-saved": ("notion-credential-error", (216, 90, 1224, 700)),
 "kit-14-error-logger-published": ("error-logger-published", (200, 0, 1440, 640)),
 "kit-21-header-auth-credential": ("header-auth-credential", (216, 90, 1224, 700)),
 "kit-22-webhook-ready": ("capture-webhook", NDV),
 "kit-23-notion-create-inbox": ("notion-create-inbox", NDV),
 "kit-26-error-workflow-pick": ("error-workflow-not-ready", (252, 98, 1236, 360)),
 "kit-27-error-workflow-set": ("error-workflow-set", (252, 98, 1188, 803)),
 "kit-28-claude-connected": ("claude-node-connected", NDV),
 "kit-29-database-link": ("notion-database-link", NDV),
 "kit-30-listening": ("waiting-for-test-call", (200, 0, 1440, 680)),
 "kit-31-test-run": ("capture-test-run", (200, 0, 1440, 680)),
 "kit-32-parsed-output": ("parse-and-validate-output", NDV),
 "kit-33-notion-error": ("notion-auth-error", NDV),
 "kit-41-button-webhook": ("button-webhook", NDV),
 "kit-51-schedule": ("schedule-trigger", NDV),
 "kit-52-notion-filter": ("notion-get-many-filter", NDV),
 "kit-61-mcp-trigger": ("mcp-server-trigger", NDV),
 "kit-62-mcp-tool": ("mcp-tool-find-tasks", NDV),
}
total = 0
for raw, (name, crop) in M.items():
    im = Image.open(f"raw/{raw}.png").convert("RGB")
    if crop: im = im.crop(crop)
    q = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    path = OUT + name + ".png"; q.save(path, optimize=True)
    total += os.path.getsize(path)
print(len(M), "images,", round(total / 1e6, 2), "MB")
