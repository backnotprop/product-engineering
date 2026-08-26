# Evidence capture

How a browser check produces a recording, checkpoints, and stills the report can play.

## Before driving anything

- Use the Playwright that is installed: `npx playwright` in a Node project, the
  `playwright` Python package elsewhere (same calls: `browser.new_context(record_video_dir=RUN, ...)`,
  `page.video.path()`). No browser binary: the item reports `skipped` with that reason
  and the run continues. The install offer belongs to the orchestrator's Scope step,
  never to a worker mid-run.
- Reach the product the way a user would. Start the local server or open the built
  artifact; wait for it to be ready; put the URL in the item's `summary`. Never drive a
  production URL unless the user named it.
- Fixed conditions, every run: viewport 1280×800, one locale, reduced motion off,
  a fresh browser context and a single page per item. A popup or second page records
  to its own file the report will not show; drive it in the same page or skip it.

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
const video = await page.video().path();     // rename to recording-<ITEM>.webm
```

The recording is `webm`; `render-report.py` converts it to `mp4` when `ffmpeg` is on
the path, and plays the `webm` otherwise. Playwright records per page, from
`newPage()`; `t0` is taken right after it, so checkpoint times line up with the frames.
Stamp `t` first, then take the still, as the helper does.

## Checkpoints

What makes a checkpoint, how many, and how to label and narrate one is in
`report-schema.md` ("Writing the fields"). The item's `summary` narrates the whole
recording.

Console errors are captured for the whole item (`page.on("console")`,
`page.on("pageerror")`). An error during a browser check is a `low` finding when it is
explained and a `flag` when it is not.

## Standalone stills

A target that was checked without a recording — a second render target, a state
reached by DOM assertion — is captured as `shot-<item>-<n>.png` and listed under
`media.screenshots` with a caption. The report shows these under the player.

## Code checks

Evidence is the thing a reader can re-run or open: `path/to/file.ts:41`, or the command
and the one output line that decided the verdict (`git diff v0.17.5 -- package.json`
shows no change to `packageManager`). Put it in the finding's `evidence`; keep the
`summary` to what was checked and what happened.
