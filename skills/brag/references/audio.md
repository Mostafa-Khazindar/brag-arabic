# Audio reference

All SFX are CC0 (Kenney.nl, public domain). Music and SFX should be used by default unless the user passes `--no-music`, `--no-sfx`, the required assets are missing, or the plan explicitly chooses silence as the strongest creative move.

Bias toward a smooth, professional result: one tasteful music bed plus a small number of well-timed SFX usually feels better than silence.

> **Note:** Audio assets are language-independent. This file is identical to the original /brag audio reference. Music and SFX work the same regardless of the text language in the video.

---

## Audio-reactive visuals

When music is present, prefer a subtle audio-reactive treatment unless the tone asks for stillness or deadpan restraint. This does not mean beat detection. It means Hyperframes can pre-extract per-frame audio data and use RMS/frequency-band energy to modulate existing visual elements.

Good uses:
- Hero glow or sky warmth breathes slightly with RMS
- Product card, phone, or metric panel gains subtle presence on bass
- Title, quote, or logo gets a soft treble glow on stronger musical moments
- Background depth, vignette, or light layer gently swells with the bed

Avoid:
- Waveform displays, equalizer bars, musical notes, or generic visualizer graphics
- Strobing, heavy pulsing, or text scaling that hurts readability
- Treating audio-reactivity as a substitute for good scene timing
- Claiming exact beat/BPM sync unless a real beat detector is available

Suggested plan notation:
```
Audio-reactive treatment: subtle; use music RMS/bass to make the hero glow and product card presence breathe. No waveform/equalizer visuals.
```

Hyperframes implementation note: follow the audio-reactive guidance owned by the `hyperframes-creative` skill (let that skill locate its own files), to extract per-frame audio data and sample it synchronously inside the composition timeline. The extraction helper ships with that skill — `/brag` does not provide it, so don't hardcode a path to it.

---

## Asset paths

All paths below are relative to `<skill-dir>`, this skill's own directory (see "Skill directory" in `SKILL.md`). It differs by install method, so resolve it rather than assuming a fixed path.

SFX live under `<skill-dir>/assets/sfx/{casino,impact,interface,ui}/`, and the individual keypress set under `<skill-dir>/assets/sfx/keyboard/`.

Music lives at `<skill-dir>/assets/music/`.

Bundled music cue presets live beside the music:

```text
<skill-dir>/assets/music/cues/<track-stem>.music-cues.md
<skill-dir>/assets/music/cues/<track-stem>.music-cues.json
```

SFX analysis lives beside the SFX library:

```text
<skill-dir>/assets/sfx/sfx-analysis.md
<skill-dir>/assets/sfx/sfx-analysis.json
```

**Critical: copy audio files into the composition project before rendering.** Hyperframes validates and serves assets from the composition directory. Always copy the files you need into `<output-dir>/composition/assets/` first:

```bash
# Create local asset dirs
mkdir -p <output-dir>/composition/assets/sfx/interface <output-dir>/composition/assets/sfx/impact <output-dir>/composition/assets/sfx/casino <output-dir>/composition/assets/sfx/ui
mkdir -p <output-dir>/composition/assets/music

# Copy only the files you plan to use (not the entire library)
cp <skill-dir>/assets/sfx/interface/bong_001.ogg <output-dir>/composition/assets/sfx/interface/
cp <skill-dir>/assets/sfx/impact/impactBell_heavy_000.ogg <output-dir>/composition/assets/sfx/impact/
cp <skill-dir>/assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3 <output-dir>/composition/assets/music/
```

Then in the composition HTML, paths are **relative to the `composition/` directory**:
```
assets/sfx/interface/bong_001.ogg
assets/sfx/impact/impactBell_heavy_000.ogg
assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3
```

Never use absolute paths (starting with `/Users/...` or `C:\Users\...`) — they will silently fail in the renderer.

---

## SFX library — approved files

The family SFX (casino, impact, interface, ui) live directly under `sfx/`; the individual keypress set lives in `sfx/keyboard/`.

Read `sfx-analysis.md` before choosing files — it lists safer picks by use case and flags files with high-frequency risk. Prefer low/medium HF risk for polished and repeated moments; reserve high-risk files for tiny isolated accents or chaotic tones.

### `keyboard/` — Individual keypress sounds

32 CC0 single keypress WAV files (`keypress-001.wav` through `keypress-032.wav`). Each is a distinct key sound at a slightly different velocity and character. Use these for per-character typing animations — randomize across the set so repeated characters don't sound robotic.

**Source:** [Keyboard Soundpack #1](https://opengameart.org/content/keyboard-soundpack-1-typing-and-single-keystrokes) by unicae_games — CC0

### `interface/` — UI sounds

| Files | Character | Use for |
|---|---|---|
| `click_001–005.ogg` | Sharp, precise | Button tap, CTA, any tap action |
| `glitch_002.ogg`, `glitch_004.ogg` | Digital distortion | Tech/AI moment, chaotic accent |
| `error_005–006.ogg` | Negative buzz | Comedic fail, wrong answer |
| `switch_001–002.ogg`, `switch_004–007.ogg` | Toggle switch | Feature switching on, binary state |
| `drop_001–003.ogg` | Soft drop | Element landing, gentle placement |
| `bong_001.ogg` | Deep bell | Dramatic announcement — use sparingly |
| `select_008.ogg` | Selection click | Navigation, item focus |

### `impact/` — Impact sounds

More physical and cinematic. Excellent for big moments and transitions.

| Files | Character | Use for |
|---|---|---|
| `impactSoft_medium_000–004.ogg` | Medium soft thud | Major reveal, hard transition — safest family |
| `impactSoft_heavy_000–004.ogg` | Heavy soft thud | Comedic bonk, weight, silly moment |
| `impactBell_heavy_000.ogg`, `_003.ogg`, `_004.ogg` | Deep resonant bell | Cinematic reveal, logo slam, dramatic moment |
| `impactPunch_heavy_000–004.ogg` | Heavy punch | Aggressive beat, chaotic tone |
| `impactPunch_medium_000–004.ogg` | Medium punch | Impact emphasis |
| `impactWood_light_000–004.ogg` | Light wood knock | Warm, organic tap |
| `impactWood_medium_000–004.ogg` | Wood knock | Warmer accent |
| `impactWood_heavy_000–004.ogg` | Heavy wood hit | Cinematic weight |
| `impactPlank_medium_000–004.ogg` | Plank slap | Comic physical moment |
| `impactPlate_heavy_000–004.ogg` | Metal plate slam | Big hit, aggressive |
| `impactPlate_light_000–004.ogg` | Light metal plate | Notification, crisp accent |
| `impactPlate_medium_000–004.ogg` | Medium plate | Mid-weight accent |
| `impactTin_medium_000–004.ogg` | Tin can hit | Quirky, lo-fi moment |
| `impactGeneric_light_000–004.ogg` | Generic light hit | Versatile small accent |
| `impactMetal_medium_000–004.ogg` | Metal tap | Medium accent |
| `impactMetal_heavy_000.ogg`, `_002.ogg`, `_004.ogg` | Heavy metal clang | Aggressive hit |
| `impactMetal_light_002–003.ogg` | Light metal ping | Small notification |
| `impactGlass_light_001–003.ogg` | Light glass clink | Sparkle, delicate achievement |
| `impactGlass_medium_000.ogg`, `_002.ogg`, `_003.ogg` | Medium glass | Moderate sparkle |

### `casino/` — Casino-style sounds

| Files | Character | Use for |
|---|---|---|
| `cardFan1–2.ogg` | Card fan | Deck reveal, spread display |
| `cardPlace1–4.ogg` | Card placement | Card landing, gentle placement |
| `cardSlide1–8.ogg` | Card slide | Card animation, dealing |
| `chipLay1–2.ogg` | Chip lay | Metric/value placement |
| `chipsCollide1–6.ogg` | Chips colliding | Stacking, accumulation |
| `chipsStack1–6.ogg` | Chips stacking | Building up, counting |
| `die*` | Dice sounds | Randomness, chance |

### `ui/` — Additional UI sounds

Read `sfx-analysis.md` for the complete list and recommendations.

---

## Music library

The bundled music is CC0/royalty-free. Check `<skill-dir>/assets/music/` for available tracks.

When selecting music, prefer tracks that:
- Have a clear energy arc (build, peak, resolve)
- Don't compete with the Arabic text overlays
- Work well at low-to-medium volume as a bed

Music is culturally neutral — the same tracks work for Arabic and English videos. If you want to use Arabic or Middle Eastern music, that's a creative choice, not a requirement. The default bundled music works well for any language.
