#!/usr/bin/env python3
"""Download audio assets from the original brag repository.

This script fetches the CC0 music and SFX files from the latent-spaces/brag
GitHub repository and places them in the correct directory structure under
skills/brag/assets/.

Usage:
    python download_assets.py
    python download_assets.py --skill-dir /path/to/skills/brag
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


REPO = "latent-spaces/brag"
BRANCH = "main"
API_BASE = f"https://api.github.com/repos/{REPO}/contents"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

# Asset directories to download
ASSET_DIRS = [
    "skills/brag/assets/music",
    "skills/brag/assets/sfx",
]


def fetch_json(url: str) -> list | dict:
    """Fetch JSON from a URL."""
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print(f"  ⚠ Rate limited by GitHub API. Try again in a few minutes, or use a token:")
            print(f"    set GITHUB_TOKEN=your_token_here")
            sys.exit(1)
        raise


def download_file(url: str, dest: Path) -> None:
    """Download a file from a URL."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(url, str(dest))
    except Exception as e:
        print(f"  ✗ Failed to download {url}: {e}")


def list_files_recursive(api_path: str) -> list[dict]:
    """Recursively list all files in a GitHub directory."""
    url = f"{API_BASE}/{api_path}?ref={BRANCH}"
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        url_with_auth = url  # Token would be in headers
    
    items = fetch_json(url)
    files = []
    
    if not isinstance(items, list):
        return files
    
    for item in items:
        if item["type"] == "file":
            files.append({
                "path": item["path"],
                "download_url": item.get("download_url") or f"{RAW_BASE}/{item['path']}",
                "size": item.get("size", 0),
            })
        elif item["type"] == "dir":
            files.extend(list_files_recursive(item["path"]))
    
    return files


def format_size(size_bytes: int) -> str:
    """Format bytes as human-readable."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download audio assets from the original brag repository"
    )
    parser.add_argument(
        "--skill-dir",
        default=None,
        help="Path to the skill directory (default: auto-detect from script location)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files that would be downloaded without downloading",
    )
    args = parser.parse_args()

    # Determine the skill directory
    if args.skill_dir:
        skill_dir = Path(args.skill_dir)
    else:
        # Auto-detect: this script is in <project>/scripts/download_assets.py
        # Skill dir is <project>/skills/brag/
        script_dir = Path(__file__).resolve().parent
        skill_dir = script_dir.parent / "skills" / "brag"

    assets_dir = skill_dir / "assets"
    print(f"🎯 Asset directory: {assets_dir}")
    print(f"📦 Source: github.com/{REPO}")
    print()

    # Check if assets already exist
    existing_count = 0
    if assets_dir.exists():
        for f in assets_dir.rglob("*"):
            if f.is_file() and f.suffix in ('.ogg', '.wav', '.mp3', '.json', '.md'):
                existing_count += 1
    
    if existing_count > 10:
        print(f"⚠ Found {existing_count} existing asset files in {assets_dir}")
        response = input("  Overwrite? [y/N] ").strip().lower()
        if response != 'y':
            print("  Aborted.")
            return

    # Discover all files
    print("🔍 Discovering files from GitHub...")
    all_files = []
    for asset_dir in ASSET_DIRS:
        try:
            files = list_files_recursive(asset_dir)
            all_files.extend(files)
            print(f"  Found {len(files)} files in {asset_dir}")
        except Exception as e:
            print(f"  ✗ Error listing {asset_dir}: {e}")

    if not all_files:
        print("✗ No files found. Check your internet connection and try again.")
        sys.exit(1)

    total_size = sum(f["size"] for f in all_files)
    print(f"\n📊 Total: {len(all_files)} files, {format_size(total_size)}")

    if args.dry_run:
        print("\n📋 Files that would be downloaded:")
        for f in all_files:
            # Map the original path to the local path
            # skills/brag/assets/... -> <skill-dir>/assets/...
            rel_path = f["path"].replace("skills/brag/", "")
            print(f"  {rel_path} ({format_size(f['size'])})")
        return

    # Download
    print(f"\n⬇ Downloading to {assets_dir}...\n")
    downloaded = 0
    failed = 0

    for f in all_files:
        # Map: skills/brag/assets/music/track.mp3 -> <skill-dir>/assets/music/track.mp3
        rel_path = f["path"].replace("skills/brag/", "")
        dest = skill_dir / rel_path

        if dest.exists():
            print(f"  ⏭ {rel_path} (exists)")
            downloaded += 1
            continue

        print(f"  ⬇ {rel_path} ({format_size(f['size'])})")
        download_file(f["download_url"], dest)
        downloaded += 1

    print(f"\n✅ Done! {downloaded} files downloaded, {failed} failed.")
    print(f"   Assets are in: {assets_dir}")


if __name__ == "__main__":
    main()
