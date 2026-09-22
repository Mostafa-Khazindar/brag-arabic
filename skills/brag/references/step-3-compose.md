# Step 3: Hand off to Hyperframes

## Create the composition brief

Write `<output-dir>/composition-brief.md` before creating or editing the Hyperframes composition.

```markdown
# Hyperframes Composition Brief: [App Name]

## Objective
Create a short launch-style brag video for [App Name] with all text in Arabic.

## Output
- Composition directory: `<output-dir>/composition/`
- Rendered video: `<output-dir>/brag.mp4`
- Format: [landscape / vertical / square] — [width]x[height]
- Duration: [15-25 seconds]
- Language: Arabic ([dialect])
- Layout direction: RTL

## Source Material
- Project root: [path]
- Primary files read: [index.html, styles.css, README, etc.]
- Product name: [name]
- Tagline / strongest claim (Arabic): [Arabic line]
- Tagline transliteration: [romanized version]
- Key UI or visual moment to recreate: [specific element]
- Copy that must appear verbatim (Arabic):
  - [Arabic line 1] — transliteration: [romanized]
  - [Arabic line 2] — transliteration: [romanized]

## Creative Direction
- Tone preset: [default / polished / yc-parody / chaotic / deadpan / cinematic / app-store]
- Creative direction: [freeform phrase, inferred or user-provided]
- Arabic dialect: [msa / egyptian / gulf / levantine / custom]
- Interpretation: [how tone affects pacing, writing, visual energy, and restraint]
- Angle: [one paragraph from brag-plan.md]
- Hook (Arabic): [first 2-3 seconds — Arabic text]
- Outro / punchline (Arabic): [final line — Arabic text]
- Avoid:
  - Generic SaaS language (in any language)
  - Abstract filler visuals
  - Unrelated visual redesign
  - Machine-translated-sounding Arabic

## Visual Identity
- Background: [exact value from project]
- Text: [exact value from project]
- Accent: [exact value from project]
- Display font: Noto Kufi Arabic [or custom choice]
- Body font: IBM Plex Sans Arabic [or custom choice]
- Monospace font: IBM Plex Mono [or custom choice]
- Visual references from the project: [short list]

## RTL Layout Requirements
- `<html lang="ar" dir="rtl">`
- All text blocks: `text-align: right`
- Flexbox layouts: `direction: rtl` or logical properties
- Mixed content (brand names, URLs, code): use `<bdi>` or `dir="ltr"` inline
- Sequential animations flow right-to-left
- Progress indicators flow right-to-left

## Arabic Typography
Load these fonts in the composition `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:wght@400;500;600;700;900&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## Storyboard
Use the storyboard in `<output-dir>/brag-plan.md` as the creative contract.

Scene summary:
1. [Scene name] — [duration]s — [Arabic text that must be seen / read]
2. [Scene name] — [duration]s — [Arabic text that must be seen / read]
3. [...]

## Audio
- Audio role: [warm bed / sparse professional accents / cinematic support / dense rhythmic layer / intentional silence]
- Audio arc: [how sound changes across the video]
- Music: [filename, or none only if disabled, missing, or intentionally silent]
- Music treatment: [volume posture, fade-in/out intent, beat/swell notes; e.g. fade under final logo]
- Music cue guidance: [cue source — bundled preset path, or "detect at composition via analyze_music_cues.py / hyperframes beats" — plus concise optional timing hints; or unavailable]
- Audio-reactive treatment: [none / subtle / expressive; what visual qualities may respond to RMS/frequency energy]
- Audio-coupled moments:
  - [scene/moment] — [typing / beat reveal / counter / card sequence / simulated interaction / final logo]
  - [scene/moment] — [intent]
- SFX selection guidance: [how sound should match motion and interaction; examples only, not rigid rules]
- SFX analysis guidance: [path to sfx-analysis.md/json if present; use lower high-frequency-risk sounds for repeated or polished moments]
- Exact SFX choice: Hyperframes should choose filenames, timestamps, density, and volume based on the implemented animation.
- Audio files: copy the chosen music and any Hyperframes-selected SFX into `<output-dir>/composition/assets/`
```

## Hyperframes Instructions

Load the composition-building Hyperframes domain skills — `hyperframes-core` (composition contract + `data-*` timing), `hyperframes-animation` (motion), `hyperframes-creative` (design spec, beats, audio-reactive), `hyperframes-keyframes` (seek-safe keyframes), and `hyperframes-cli` (lint/check/render). /brag is its own workflow: do not enter the `hyperframes` entry-point intent interview and do not route into its generic promo / launch-video workflow. Prefer native Hyperframes conventions over anything in `/brag`.

Requirements:
- **All text overlays must be in Arabic** with proper RTL rendering.
- The composition HTML must use `<html lang="ar" dir="rtl">`.
- Show at least one real UI, copy, or visual element from the source project.
- Keep all text readable in the final render. Arabic text needs slightly more line-height (1.5-1.7) than Latin text.
- Keep the video within 15-25 seconds.
- Include the planned music/SFX layer unless audio was explicitly disabled or documented as intentionally silent.
- Treat `/brag` audio notes as guidance, not a fixed cue sheet. Choose SFX after the visual animation exists.
- Treat music cue metadata as optional timing hints. Hyperframes decides exact animation timing and should ignore cues that hurt readability, scene pacing, or the product story.
- Major reveals may move toward nearby strong cues within about 0.15s. Smaller entrances may align to nearby beat points within about 0.10s. Use only 1-3 strong cue locks in a 15-25s video unless the edit clearly benefits from more.
- Use SFX to support motion and interaction: card sounds for card-like reveals, short announcement cues for major payoffs, key/click sounds for text or user actions, and restraint when the edit is already busy.
- Honor planned music treatment such as fade-outs, ducking, beat-aligned reveals, or letting a final SFX ring over the music, using the best Hyperframes-supported implementation.
- When music is present and the treatment is not `none`, consider Hyperframes audio-reactive workflow: extract audio data and use RMS/frequency bands for subtle, brand-specific motion. Good targets are glow, depth, background warmth, card presence, title emphasis, or other existing visual elements. Avoid waveform/equalizer visuals, musical-note graphics, generic particle systems, strobing, or heavy pulsing.
- Use local assets for audio and any required runtime/media.

### RTL-specific composition rules

1. **Text alignment**: All Arabic text elements use `text-align: right` by default.
2. **Layout flow**: Flex containers use `flex-direction: row-reverse` or `direction: rtl` for horizontal layouts.
3. **Animations**: Slide-in animations come from the left (opposite of English), fade-ins are direction-neutral.
4. **Mixed content**: When showing code, terminal output, or English brand names alongside Arabic text, wrap them in `<bdi dir="ltr">` elements.
5. **Line height**: Arabic text needs `line-height: 1.5` minimum (ideally 1.6-1.7) for readability, especially for Naskh-style fonts.
6. **Letter spacing**: Arabic text should have `letter-spacing: 0` or slightly negative — never positive letter-spacing like Latin display text.
7. **Word spacing**: Arabic words can be spaced normally. No special treatment needed.
