# Evidence capture

How a browser check produces a recording, checkpoints, and stills the report can play.

## Before driving anything

- Use the Playwright that is installed: `npx playwright` in a Node project, the
  `playwright` Python package elsewhere. When no browser binary exists, offer one line
  — `npx playwright install chromium` — and wait for a yes. Declined or unavailable:
  the browser items report `skipped` with that reason, and the run continues.
- Reach the product the way a user would. Start the local server or open the built
  artifact; wait for it to be ready; put the URL in the item's `summary`. Never drive a
  production URL unless the user named it.
- Fixed conditions, every run: viewport 1280×800, one locale, reduced motion off,
  a fresh browser context per item. Same inputs, same recording.

## Recording

Record at the context level so the video covers the whole item:

```js
const context = await browser.newContext({
  viewport: { width: 1280, height: 800 },
  recordVideo: { dir: RUN, size: { width: 1280, height: 800 } },
});
const page = await context.newPage();
const t0 = Date.now();
const checkpoints = [];
async function checkpoint(label, narration) {
  const t = (Date.now() - t0) / 1000;
  const screenshot = `cp-${ITEM}-${checkpoints.length + 1}.png`;
  await page.screenshot({ path: `${RUN}/${screenshot}` });
  checkpoints.push({ t: Math.round(t * 10) / 10, label, narration, screenshot });
}
// ... drive the product, calling checkpoint() at each moment that matters ...
await context.close();                       // flushes the video file
const video = await page.video().path();     // rename to recording-<item>.webm
```

The recording is `webm`; `render-report.py` converts it to `mp4` when `ffmpeg` is on
the path, and plays the `webm` otherwise. The video's clock starts when the context
opens, so checkpoint times taken from the same moment line up with the frames.

## Checkpoints

A checkpoint is a moment the reader would want to jump to: the page loaded, the thing
rendered, the action landed, the result appeared. Three to six per recording.

- `label`: what is visible at that moment, in a few words — "Toolbar renders",
  "Comment added".
- `narration`: one sentence saying what the still shows and why it matters to the
  check.
- Times ascend. Take the still at the checkpoint, not after the next step.

Console errors are captured for the whole item (`page.on("console")`,
`page.on("pageerror")`). An error during a browser check is a `low` finding when it is
explained and a `flag` when it is not.

## Standalone stills

A target that was checked without a recording — a second render target, a state
reached by DOM assertion — gets a `screenshots` entry with a caption. The report shows
these under the player; they are evidence, not decoration.

## Code checks

Evidence is the thing a reader can re-run or open: `path/to/file.ts:41`, or the command
and the one output line that decided the verdict (`git diff v0.17.5 -- package.json`
shows no change to `packageManager`). Put it in the finding's `evidence`; keep the
`summary` to what was checked and what happened.

## What the report needs from all of this

Per item: `media.video` (relative to the run folder), `media.checkpoints[]` as
collected above, optional `media.screenshots[]`, and findings whose `evidence`
points at a timestamp (`recording 0:16`) or a file:line. The contract with every
field and rule is `report-schema.md`; validate before rendering.
