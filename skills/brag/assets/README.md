# Audio Assets

This directory should contain the CC0 music and SFX files from the original [/brag](https://github.com/latent-spaces/brag) project.

## Quick setup

Run the download script from the project root:

```bash
python scripts/download_assets.py
```

## Directory structure

After downloading, this directory should contain:

```
assets/
├── music/
│   ├── *.mp3              # CC0 music tracks
│   └── cues/
│       ├── *.music-cues.json   # Pre-computed beat/cue metadata
│       └── *.music-cues.md     # Human-readable cue summaries
└── sfx/
    ├── casino/            # Card, chip, dice sounds
    ├── impact/            # Impact, bell, punch, wood sounds
    ├── interface/         # Click, switch, drop, UI sounds
    ├── keyboard/          # Individual keypress WAV files
    ├── ui/                # Additional UI sounds
    ├── sfx-analysis.json  # SFX metadata
    └── sfx-analysis.md    # Human-readable SFX guide
```

## Licenses

- Music: CC0 / royalty-free
- SFX: CC0 ([Kenney.nl](https://kenney.nl/), [OpenGameArt](https://opengameart.org/))
- Keyboard sounds: CC0 by unicae_games

All assets are language-independent and identical to the original /brag project.
