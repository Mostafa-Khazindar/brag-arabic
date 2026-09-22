# Step 4: Validate, render, and deliver

## Validate

```bash
cd <output-dir>/composition
npx hyperframes check   # brag's single pre-render gate — fix every error it reports
```

Fix all errors. `check` is brag's single pre-render gate — run it and fix everything it reports, including WCAG contrast failures (they gate as errors, not warnings). Each contrast finding carries a suggested compliant color, so apply it or adjust within the palette family and re-run `check` — most fixes need no screenshot. There is no per-element contrast escape hatch for real text; the only bypass is `check --no-contrast`, which skips the entire WCAG pass (all-or-nothing), not a way to accept one borderline element. For exact contrast thresholds, layout escape hatches, and reporting details, follow the current hyperframes-cli `check` guidance. `check`'s layout pass backstops the "keep all text readable" creative law — fix any reported overflow.

### Arabic-specific validation

After `npx hyperframes check` passes, verify:

1. **RTL rendering**: Ensure `dir="rtl"` is present on the `<html>` element.
2. **Font loading**: Verify Arabic fonts are loaded (Noto Kufi Arabic, IBM Plex Sans Arabic).
3. **Text overflow**: Arabic text may wrap differently than English. Check that no Arabic text is clipped or overflows its container.
4. **Mixed direction**: If the composition includes English brand names or code alongside Arabic text, verify they render correctly with `<bdi>` or inline `dir="ltr"`.
5. **Line height**: Arabic text should have adequate line-height (1.5+) for readability.

For a visual gut-check before rendering, optionally capture key frames:

```bash
npx hyperframes snapshot   # PNG key frames
```

## Preview

```bash
npx hyperframes preview
```

Tell the user the preview is running and give them the localhost URL. Invite them to check it before rendering.

If the user approves or asks to render:

## Render

```bash
npx hyperframes render --output ../brag.mp4
```

This outputs to `<output-dir>/brag.mp4` (one level up from the composition directory).

For a faster iteration render:
```bash
npx hyperframes render --quality draft --output ../brag.mp4
```

For final delivery:
```bash
npx hyperframes render --quality high --output ../brag.mp4
```

## Pick the poster frame

The poster is the still shown before the video plays — the first thing anyone sees when it's idle or unplayed. Don't leave it to the raw first frame or an arbitrary timestamp; those land on fades, mid-transitions, blank intro backgrounds, or half-rendered text.

You built this composition, so you already know its strongest moment and exactly when it lands — the hook line, the hero reveal, or the final logo. Pick that beat at a **settled** point: text fully animated in, before it exits (the storyboard timings tell you the safe window). Then extract that one frame full-res with ffmpeg. From `<output-dir>/composition`:

```bash
# use the timestamp of your strongest settled beat, e.g. 3.2s
ffmpeg -ss 3.2 -i ../brag.mp4 -frames:v 1 -q:v 2 ../brag.jpg
```

Aim for a frame that's postable on its own — and that shows Arabic text clearly rendered and readable. For Arabic compositions, pick a frame where the Arabic headline or hook is fully visible and settled, not mid-animation. If the pulled frame lands on a transition or mid-animation, nudge the timestamp a few tenths of a second and re-extract.

### Bake the poster as frame 0

A bare `.mp4` has no `poster` attribute — every player and platform picks its own idle thumbnail, and almost all of them grab **frame 0**. Slack, Twitter/X, and Discord regenerate thumbnails server-side from the video itself, so the only reliable way to control the idle image everywhere is to prepend the poster as a held frame at the very start of the file.

```bash
# from <output-dir>/composition — adjust 3.2 to your best frame time
ffmpeg -ss 3.2 -i ../brag.mp4 -frames:v 1 -q:v 2 ../brag-poster.jpg
ffmpeg -loop 1 -t 0.04 -i ../brag-poster.jpg \
       -i ../brag.mp4 \
       -filter_complex "[0:v]scale=WIDTH:HEIGHT:force_original_aspect_ratio=decrease,pad=WIDTH:HEIGHT:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=30[poster];[1:v]setsar=1,fps=30[main];[poster][main]concat=n=2:v=1:a=0[v]" \
       -map "[v]" -map 1:a? \
       -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p \
       -c:a copy \
       -movflags +faststart \
       ../brag-final.mp4
mv ../brag-final.mp4 ../brag.mp4
rm ../brag-poster.jpg
```

Replace `WIDTH` and `HEIGHT` with the composition dimensions.

## Write the share copy

Write `<output-dir>/share-copy.md` with social media copy in Arabic:

```markdown
# Share Copy — [App Name]

## Arabic (primary)
[Arabic share copy — 1-2 punchy sentences for X/Twitter, LinkedIn, Discord]

## Transliteration
[Romanized version of the Arabic copy for non-Arabic speakers]

## English (reference)
[English version of the same copy, for the developer's own understanding]

## Hashtags
[2-3 relevant hashtags, mix of Arabic and English]
#[Arabic hashtag] #[English hashtag]
```

The share copy must:
- Be in Arabic, in the selected dialect
- Sound natural — not translated
- Be punchy and social-media-ready
- Include a transliteration so non-Arabic-speaking developers know what it says
- Include an English reference translation
