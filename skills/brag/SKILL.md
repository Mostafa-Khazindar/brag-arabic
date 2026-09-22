---
name: brag
description: "Arabic /brag — Turn the current project into a short, polished, shareable launch video with all text, copy, and narration in Arabic. Use when someone says \"/brag\", \"let's brag about this\", \"make a launch video\", or wants to share what they built with Arabic-speaking audiences. Reads the project code directly — no live URL or screenshots needed. Works for any developer, Arabic-speaking or not."
---

# /brag (Arabic)

You built it. Now let's brag about it — in Arabic.

This is the Arabic localization of `/brag`. It produces the same high-quality launch videos as the original, but all **generated text** — headlines, taglines, scene overlays, share copy, and narration — is in Arabic.

**This skill is for everyone.** You don't need to speak Arabic to use it. If you're a developer who wants to show off your work to Arabic-speaking stakeholders, clients, or audiences, this skill handles the Arabic for you.

## Invocation dispatch (must happen first)

Before inspecting the project, parse the complete `/brag` invocation. If the
invocation contains `--voice`, set `voice.enabled = true`. Enable narration
only for that run. Do not enable narration automatically and do not fall back
to the normal no-voice workflow.

`/brag` turns the current project website or app into a short, polished, shareable launch video using Hyperframes — with all generated text in Arabic. It is narrow, opinionated, and fun.

## What this skill does

1. Reads the current project code to understand the app (in any language).
2. Plans a short brag concept specific to this project.
3. Scripts and storyboards the video — all text overlays and copy in Arabic.
4. Hands a focused composition brief to Hyperframes with RTL layout.
5. Validates, renders, and writes share copy in Arabic.

## Arabic output rules

All text that appears in the final video and share copy **must be in Arabic**. This includes:

- Video text overlays (headlines, taglines, feature callouts)
- Scene text and captions
- Share copy for social media
- Narration script (when `--voice` is enabled)

The following stay in their original language (usually English):
- Code snippets shown in the video
- URLs, domain names, brand names that are inherently Latin-script
- Terminal commands
- The agent's internal reasoning and plan files (English for debugging)

### Arabic quality guidelines

- Use fluent, natural Arabic. Avoid word-for-word translation from English.
- Prefer concise Arabic phrasing. Arabic is naturally more compact than English for marketing copy.
- Product names and technical terms may stay in their original language, wrapped in Arabic sentence structure.
- Numbers use Eastern Arabic numerals (٠١٢٣٤٥٦٧٨٩) for body text, but Western numerals (0123456789) are acceptable for metrics and statistics.

## Parsing the invocation

The user may invoke with natural language or flags:

```
/brag
/brag --tone chaotic
/brag --tone polished --format vertical
/brag --dialect gulf
/brag --dialect egyptian --tone yc-parody
/brag this. Make it feel like a ridiculous startup launch.
```

Parse these options:

| Option | Values | Default |
|---|---|---|
| `--tone` | preset or freeform description | inferred |
| `--format` | `landscape`, `vertical`, `square` | `landscape` |
| `--duration` | seconds | auto (15-25s) |
| `--no-music` | flag | music on |
| `--no-sfx` | flag | sfx on |
| `--title` | string | inferred from project |
| `--voice` | flag | narration off |
| `--dialect` | `msa`, `egyptian`, `gulf`, `levantine`, or freeform | `msa` |

### Dialect handling

The `--dialect` flag controls the Arabic register used in generated text:

| Value | Description | Example |
|---|---|---|
| `msa` (default) | Modern Standard Arabic (فصحى حديثة). Professional, universally understood. Best for corporate and formal audiences. | بنيناه. والآن حان وقت التفاخر. |
| `egyptian` | Egyptian Arabic (عامية مصرية). Warm, conversational, widely understood across the Arab world. Best for casual/social media. | بنيناه. ودلوقتي وقت الفشخرة. |
| `gulf` | Gulf Arabic (خليجي). Professional with Gulf flavor. Best for GCC audiences. | بنيناه. والحين وقت الفخر. |
| `levantine` | Levantine Arabic (شامي). Conversational, modern. Best for Levant audiences. | بنيناه. وهلق وقت نتفاخر. |
| freeform | Any description the user provides (e.g., "formal Quranic style", "Moroccan darija"). Map to the nearest preset for structure but preserve the direction. | varies |

When no dialect is specified, default to MSA. MSA is the safe default — it's understood everywhere and works for professional contexts.

Voice is opt-in. If `--voice` is present, use Kokoro via Hyperframes and do
not add any provider-selection logic. The voice workflow is intentionally
single-provider. The narration script must be in the selected Arabic dialect.

Tone can be a preset (`default`, `polished`, `yc-parody`, `chaotic`, `deadpan`, `cinematic`, `app-store`) or a creative direction such as "fake Series A launch from 2016", "museum exhibit", or "overproduced mobile game ad".

When the user gives freeform tone direction, map it to the nearest preset for pacing and structure, but preserve the user's direction in the plan and composition brief.

## Narration guidance

When `--voice` is enabled, write narration in Arabic that complements the visuals, does
not simply read visible text, matches scene pacing, sounds natural and
conversational in the selected dialect, and moves smoothly between scenes. Keep the script concise and
specific to the product so the voice feels like part of the edit rather than a
separate narration track.

---

## Output directory

By default, output goes to `brag-output/`. To avoid overwriting previous runs, use a timestamped directory:

```
brag-output-2026-05-04-143022/
```

Use a timestamp when:
- The user explicitly asks for a new run without overriding previous results
- A `brag-output/` directory already exists in the project

Generate the timestamp at the start of the run (`YYYY-MM-DD-HHmmss`) and use it consistently for all output paths in that run: plan, brief, composition, render, and share copy.

## Skill directory

`<skill-dir>` is the directory containing this `SKILL.md`. Claude Code prints it as "Base directory for this skill" when the skill loads; for other agents it's wherever the skill was installed. Bundled assets are under `<skill-dir>/assets/` and scripts under `<skill-dir>/scripts/`. Don't guess an install path: a plugin install, a `~/.claude/skills/` copy, and this repo all put it somewhere different.

---

## Typography — Arabic font stack

All Hyperframes compositions must load Arabic-capable web fonts. The default stack:

### Display font (headlines, hero text)
```
font-family: "Noto Kufi Arabic", "Arial", sans-serif;
```

### Body font (descriptions, feature text)
```
font-family: "IBM Plex Sans Arabic", "Noto Naskh Arabic", "Arial", sans-serif;
```

### Monospace (code, terminal, metrics)
```
font-family: "IBM Plex Mono", "Geist Mono", ui-monospace, monospace;
```

Load via Google Fonts in the composition HTML `<head>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Noto+Kufi+Arabic:wght@400;500;600;700;900&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Noto+Naskh+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet" />
```

## RTL layout rules

Every Hyperframes composition HTML must include:

```html
<html lang="ar" dir="rtl">
```

Additional RTL rules:
- `text-align: right` is the default for Arabic text
- Flexbox/grid layouts should use `direction: rtl` or logical properties (`margin-inline-start` instead of `margin-left`)
- Mixed content (English brand names, code, URLs) should use `<bdi>` or `dir="ltr"` inline
- Progress bars, timelines, and sequential animations flow right-to-left
- Icon placement follows RTL conventions (arrows point left for "forward")

---

## Step 1: Inspect the project

**Read:** [references/step-1-inspect.md](references/step-1-inspect.md)

## Step 2: Write the brag plan

**Read:** [references/step-2-plan.md](references/step-2-plan.md)

After reading the reference, write `<output-dir>/brag-plan.md` with all scene text, headlines, and share copy in Arabic.

## Step 3: Hand off to Hyperframes

**Read:** [references/step-3-compose.md](references/step-3-compose.md)

After reading the reference, write `<output-dir>/composition-brief.md`. Then create the composition with RTL layout and Arabic typography.

## Step 4: Validate, render, and deliver

**Read:** [references/step-4-deliver.md](references/step-4-deliver.md)

After reading the reference, validate with `npx hyperframes check`, render, and deliver the final video with Arabic share copy.

## Done

Tell the user:

```
✅ /brag complete — Arabic launch video ready.

📁 Output: <output-dir>/
🎬 Video: <output-dir>/brag.mp4
🖼️ Poster: <output-dir>/brag.jpg

📋 Share copy (Arabic):
<the Arabic share copy line>

📋 Share copy (transliterated):
<romanized version for non-Arabic speakers to verify>
```

Provide both the Arabic share copy and a romanized/transliterated version so non-Arabic-speaking developers can at least read it phonetically and verify it makes sense.
