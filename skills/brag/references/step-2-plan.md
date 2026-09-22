# Step 2: Write the brag plan

Write `<output-dir>/brag-plan.md`. One focused page. This is the creative north star for the entire video.

The plan should specify what the video must communicate and what project material must be used. It should not prescribe low-level Hyperframes implementation details. Hyperframes will decide the concrete composition structure, animation mechanics, and render workflow from the brief in Step 3.

**All scene text, headlines, taglines, and share copy in the plan must be in Arabic**, in the dialect specified by `--dialect` (default: MSA). Internal notes and structural labels may remain in English for readability.

## Create the output directory

```bash
mkdir -p <output-dir>
```

## Structure of brag-plan.md

```markdown
# Brag Plan: [App Name]

## What is this app?
[One sentence in English. What it does, what makes it funny or impressive.]

## The angle
[The creative premise in English. The joke, the hook, the claim.
What makes this video specific to this project and not generic.]

## Arabic dialect
[msa / egyptian / gulf / levantine / custom description]

## Hook (first 2-3 seconds)
[The opening moment — IN ARABIC. This is the most important decision.
What Arabic word, phrase, or motion earns the next 20 seconds?]
Transliteration: [romanized version for non-Arabic speakers]

## Key moments (the middle)
[2-3 sharp highlights from the product — text overlays IN ARABIC.
Bullet points. Specific. "عداد الارتفاع يصعد" not "feature callouts."]
- [Arabic text] — transliteration: [romanized]
- [Arabic text] — transliteration: [romanized]
- [Arabic text] — transliteration: [romanized]

## Outro / punchline
[How does it land? The final line IN ARABIC. The beat before the logo.]
Transliteration: [romanized version]

## User flow worth showing
[The 2–3 beats of *using* the product (entry → key action → result), pulled from
Step 1 question 9. This is the strongest material the video has — the centerpiece
scenes should show the flow, not just landing-page sections. If the project is
landing-page-only, write "none — landing-page only" and rely on Key moments instead.]

## Tone
- Preset: [default / polished / yc-parody / chaotic / deadpan / cinematic / app-store]
- Creative direction: [freeform phrase, inferred or user-provided]
- Interpretation: [one sentence on how this affects pacing, writing, visual energy, and restraint]

## Format: [landscape / vertical / square] — [width]x[height]
## Duration: [target seconds]

## Visual identity (from the project)
- Background: [exact color value]
- Accent: [exact color value]
- Text: [exact color value]
- Display font: [Arabic font — default: Noto Kufi Arabic]
- Body font: [Arabic font — default: IBM Plex Sans Arabic]
- Monospace font: [for code/metrics — default: IBM Plex Mono]
- Strongest visual element: [what from the site to reference]
- Layout direction: RTL

## Share copy (Arabic — draft)
[One or two sentences for Twitter/X/LinkedIn/Discord. IN ARABIC. Punchy. Not corporate.]
Transliteration: [romanized version for non-Arabic speakers to verify]

## Audio direction
- Role: [warm bed / sparse professional accents / cinematic support / dense rhythmic layer / intentional silence]
- Music: [candidate track / mood / none only if disabled, missing, or intentionally silent]
- Music treatment: [start time, volume posture, fade-in/out intent, beat/swell notes]
- Music cue guidance: [preset cue file read / unavailable; list 1-3 strongCue timestamps for major moments; list beat-grid windows for sequential events]
- Audio-reactive treatment: [none / subtle / expressive; what visual qualities may respond to music energy]
- SFX posture: [sparse / moderate / dense; motion-matched; professional restraint]
- Audio-coupled moments: [visual ideas that should consider sound, e.g. typed text, beat reveal, count-up, card sequence]
- Restraint rule: [what audio must not do]

## Storyboard

### Scene 1 — [name] — [duration]s
[What's on screen. What Arabic text appears. What product material must be referenced.]
Arabic text: [the exact Arabic text that appears on screen]
Transliteration: [romanized version]
Sequential/interaction: [yes — describe what appears one by one or what interaction is simulated; or none]
Audio intent: [what the sound should do emotionally]
Audio-coupled idea: [typed text, beat-aligned reveal, counter ticks, card-by-card sequence, simulated tap/swipe/type — or none]
Music: [mood, or "none" only if disabled / missing / intentionally silent]
Transition mood: [clean / hard / dramatic / soft / chaotic] → Scene 2

### Scene 2 — [name] — [duration]s
[...]
Arabic text: [the exact Arabic text]
Transliteration: [romanized version]
Sequential/interaction: [yes — describe it; or none]
Audio intent: [what the sound should do emotionally]
Audio-coupled idea: [type or none]
Transition mood: [mood] → Scene 3

[... continue for all scenes]

**Music mood for this video:** [upbeat / cinematic / chaotic / deadpan / parody / none only if disabled / missing / intentionally silent]
**Audio summary:** [one sentence describing the full audio arc]
```

## Planning the scenes

The default pattern is:
```
Hook → Reveal → 2-3 highlights → Punchline/outro
```

But adapt it. These are the right scene counts for each tone:

| Tone | Scenes | Pacing |
|---|---|---|
| `default` | 4-5 | Comfortable. Room for each moment to breathe. |
| `polished` | 3-4 | Fewer scenes, longer holds. Confidence through restraint. |
| `yc-parody` | 4-5 | Structured. The joke is how seriously it's delivered. |
| `chaotic` | 6-8 | Rapid. Some scenes under 2 seconds. |
| `deadpan` | 3-4 | Long holds. Big empty space. One word at a time. |
| `cinematic` | 4-5 | Wide shots. Big type. Dramatic reveals. |
| `app-store` | 4-6 | Feature cards. Clean reveals. No mess. |

## Duration guidance

Scene durations must sum to 15-25 seconds. Count them.

- Under 15 seconds: too thin, add a scene or lengthen holds.
- Over 25 seconds: cut a scene or tighten timing.
- 18-22 seconds is the sweet spot for most brag videos.

## Reading time — Arabic considerations

Arabic text is typically shorter than English for the same meaning, but Arabic script is denser and may require slightly more reading time for unfamiliar readers.

High pace comes from fast motion, fast transitions, and tight cuts — NOT from pulling text off screen before it can be read. Every text element a viewer must read needs enough fully-visible, settled time (entered, not yet exiting) to actually read it:

- Short label or 1-3 word Arabic line: about 1.0s settled (slightly more than English due to script density).
- Headline or full Arabic sentence: about 0.35s per word, minimum ~1.4s. The hook line gets the most.

Plan that floor, then keep everything else fast: entrances and transitions stay snappy (0.3-0.6s) and motion stays energetic. A line can SLAM in fast and then HOLD — fast entrance, generous hold, fast exit.

## Arabic copy guidelines

When writing Arabic text for scenes:

1. **Don't translate — reimagine.** Take the English meaning and write what an Arabic copywriter would write. Arabic marketing copy has its own rhythm and punch.

2. **Keep it short.** Arabic is naturally more compact. Use that. Fewer words, bigger impact.

3. **Match the dialect.** If `--dialect egyptian` was specified, the hook line "بنيناه" becomes "بنيناه" (same in this case, but tone words change). Gulf might say "سويناه". Levantine might say "عملناه".

4. **Brand names stay as-is.** Don't transliterate "GitHub" to "غيتهب" unless the project itself does. Keep brand names in Latin script, wrapped in Arabic sentence structure.

5. **Numbers are flexible.** Use Eastern Arabic numerals (٣٫٥ مليون) for a more Arabic feel, or Western numerals (3.5M) for tech audiences. Match the project's existing style.

6. **Provide transliterations.** Every piece of Arabic copy in the plan must have a romanized transliteration so non-Arabic-speaking developers can verify the content makes sense.
