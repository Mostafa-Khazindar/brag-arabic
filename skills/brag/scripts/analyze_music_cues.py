#!/usr/bin/env python3
"""Generate music cue metadata (tempo, beat grid, strong cues) for any track.

Used two ways: (1) a maintainer tool to precompute the bundled-track cue
presets, and (2) an optional runtime "extended" beat-sync path for /brag on
any track when Python + librosa are available (see references/audio.md ->
"Beat and cue sources"). When those deps are absent, /brag falls back to
`npx hyperframes beats`. Takes any audio file as input.

This script is language-independent — it analyzes audio features, not text.
Identical to the original /brag version.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import librosa
import numpy as np


HOP_LENGTH = 512
FRAME_LENGTH = 2048
BASS_N_FFT = 4096
BASS_MIN_HZ = 30.0
BASS_MAX_HZ = 180.0


def _as_float(value: Any) -> float:
    array = np.asarray(value)
    if array.size == 0:
        return 0.0
    return float(array.reshape(-1)[0])


def _finite_round(value: float, digits: int = 4) -> float:
    if not math.isfinite(value):
        return 0.0
    return round(float(value), digits)


def _normalize(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    values = np.nan_to_num(values, nan=0.0, posinf=0.0, neginf=0.0)
    if values.size == 0:
        return values
    values = np.maximum(values, 0.0)
    high = np.percentile(values, 98)
    if high <= 1e-12:
        high = np.max(values)
    if high <= 1e-12:
        return np.zeros_like(values)
    return np.clip(values / high, 0.0, 1.0)


def _feature_at(feature: np.ndarray, frame: int) -> float:
    if feature.size == 0:
        return 0.0
    index = int(np.clip(frame, 0, feature.size - 1))
    return float(feature[index])


def _local_contrast(onset_norm: np.ndarray, frame: int, sr: int) -> float:
    radius = max(1, int(round(0.5 * sr / HOP_LENGTH)))
    start = max(0, frame - radius)
    end = min(onset_norm.size, frame + radius + 1)
    local = onset_norm[start:end]
    if local.size == 0:
        return 0.0
    median = float(np.median(local))
    return max(0.0, _feature_at(onset_norm, frame) - median)


def _score_frame(
    frame: int,
    onset_norm: np.ndarray,
    contrast_norm: np.ndarray,
    rms_norm: np.ndarray,
    bass_norm: np.ndarray,
) -> dict[str, float]:
    onset = _feature_at(onset_norm, frame)
    contrast = _feature_at(contrast_norm, frame)
    rms = _feature_at(rms_norm, frame)
    bass = _feature_at(bass_norm, frame)
    intensity = 0.45 * onset + 0.25 * contrast + 0.20 * rms + 0.10 * bass
    return {
        "intensity": float(np.clip(intensity, 0.0, 1.0)),
        "onsetStrength": onset,
        "localOnsetContrast": contrast,
        "rms": rms,
        "bassEnergy": bass,
    }


def _dedupe_cues(cues: list[dict[str, Any]], min_gap: float = 0.18) -> list[dict[str, Any]]:
    sorted_by_strength = sorted(cues, key=lambda item: item["intensity"], reverse=True)
    accepted: list[dict[str, Any]] = []
    for cue in sorted_by_strength:
        if all(abs(cue["time"] - existing["time"]) >= min_gap for existing in accepted):
            accepted.append(cue)
    return sorted(accepted, key=lambda item: item["time"])


def _compact_times(items: list[dict[str, Any]], max_items: int = 48) -> str:
    subset = items[:max_items]
    text = ", ".join(f"{item['time']:.2f}" for item in subset)
    if len(items) > max_items:
        text += f", ... (+{len(items) - max_items} more)"
    return text


def analyze(audio_path: str | Path) -> dict[str, Any]:
    """Analyze an audio file and return cue metadata."""
    path = Path(audio_path)
    y, sr = librosa.load(str(path), sr=None, mono=True)
    duration = float(librosa.get_duration(y=y, sr=sr))

    # Tempo and beat grid
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, hop_length=HOP_LENGTH)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr, hop_length=HOP_LENGTH)
    bpm = _finite_round(_as_float(tempo))

    # Onset strength
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=HOP_LENGTH)
    onset_norm = _normalize(onset_env)

    # Local contrast for each beat
    contrast_raw = np.array([_local_contrast(onset_norm, f, sr) for f in beat_frames])
    contrast_norm = _normalize(contrast_raw)

    # RMS energy
    rms_raw = librosa.feature.rms(y=y, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH)[0]
    rms_norm = _normalize(rms_raw)

    # Bass energy
    S = np.abs(librosa.stft(y, n_fft=BASS_N_FFT, hop_length=HOP_LENGTH))
    freqs = librosa.fft_frequencies(sr=sr, n_fft=BASS_N_FFT)
    bass_mask = (freqs >= BASS_MIN_HZ) & (freqs <= BASS_MAX_HZ)
    bass_energy = S[bass_mask, :].sum(axis=0) if bass_mask.any() else np.zeros(S.shape[1])
    bass_norm = _normalize(bass_energy)

    # Score each beat
    beat_cues = []
    for i, frame in enumerate(beat_frames):
        t = _finite_round(float(beat_times[i]), 3)
        scores = _score_frame(frame, onset_norm, contrast_norm, rms_norm, bass_norm)
        beat_cues.append({"time": t, "beatIndex": i, **{k: _finite_round(v) for k, v in scores.items()}})

    # Strong cues: top intensity beats, deduped
    threshold = 0.55
    strong = [c for c in beat_cues if c["intensity"] >= threshold]
    if len(strong) < 3:
        strong = sorted(beat_cues, key=lambda c: c["intensity"], reverse=True)[:5]
    strong_cues = _dedupe_cues(strong)

    return {
        "file": path.name,
        "duration": _finite_round(duration, 2),
        "bpm": bpm,
        "beatCount": len(beat_cues),
        "beatGrid": beat_cues,
        "strongCues": strong_cues,
        "summary": {
            "beats": _compact_times(beat_cues),
            "strongCues": _compact_times(strong_cues),
        },
    }


def write_outputs(result: dict[str, Any], output_dir: Path, stem: str) -> None:
    """Write JSON and markdown cue files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / f"{stem}.music-cues.json"
    json_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))

    md_lines = [
        f"# Music Cues: {result['file']}",
        "",
        f"- **Duration:** {result['duration']}s",
        f"- **BPM:** {result['bpm']}",
        f"- **Beats:** {result['beatCount']}",
        "",
        "## Strong Cues",
        "",
        "| Time | Intensity | Onset | Contrast | RMS | Bass |",
        "|------|-----------|-------|----------|-----|------|",
    ]
    for cue in result["strongCues"]:
        md_lines.append(
            f"| {cue['time']:.2f}s | {cue['intensity']:.3f} | "
            f"{cue['onsetStrength']:.3f} | {cue['localOnsetContrast']:.3f} | "
            f"{cue['rms']:.3f} | {cue['bassEnergy']:.3f} |"
        )
    md_lines.extend(["", "## Beat Grid (times)", "", result["summary"]["beats"]])

    md_path = output_dir / f"{stem}.music-cues.md"
    md_path.write_text("\n".join(md_lines))

    print(f"  JSON: {json_path}")
    print(f"  Markdown: {md_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze music cues for /brag")
    parser.add_argument("audio", help="Path to audio file")
    parser.add_argument("--output-dir", "-o", default=None, help="Output directory for cue files")
    args = parser.parse_args()

    audio_path = Path(args.audio)
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    output_dir = Path(args.output_dir) if args.output_dir else audio_path.parent / "cues"
    stem = audio_path.stem

    print(f"Analyzing: {audio_path}")
    result = analyze(audio_path)
    print(f"  BPM: {result['bpm']}, Beats: {result['beatCount']}, Strong cues: {len(result['strongCues'])}")

    write_outputs(result, output_dir, stem)
    print("Done.")


if __name__ == "__main__":
    main()
