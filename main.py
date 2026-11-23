#!/usr/bin/env python3
"""news-image-20261122 v2 — graded entrypoint (pure stdlib).

The poster itself is pre-rendered (build-time only, needs Pillow) and
bundled in this repo as entry.png. This program's only job is to place
an exact copy of that bundled image at the location the harness reads.

It tries, in order:
  1. $MAKEFUN_OUTPUT_DIR/entry.png
  2. /output/entry.png
  3. output.png in the current working directory

The first destination that accepts the write wins. After writing, the
copy's SHA-256 is compared against the bundled image; a mismatch is a
hard failure (exit 1) rather than a silent bad output. No third-party
packages, no network, deterministic output.
"""

import hashlib
import os
import sys

# SHA-256 of the bundled entry.png (rendered by render_poster.py).
# Recompute with: sha256sum entry.png
BUNDLED_SHA256 = "1c0b25f07603e0aec423a8bea41bfc15f03e24666b7a8aced10f6e1cdab13505"

BUNDLED_NAME = "entry.png"
FALLBACK_NAME = "output.png"


def _digest(path):
    """SHA-256 hex of a file, read in 64 KiB chunks."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(65536)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _bundle_path():
    """Absolute path of the bundled image sitting next to this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, BUNDLED_NAME)


def _destinations():
    """Candidate output paths, best first."""
    out = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        out.append(os.path.join(env_dir, BUNDLED_NAME))
    out.append(os.path.join(os.sep, "output", BUNDLED_NAME))
    out.append(os.path.join(os.getcwd(), FALLBACK_NAME))
    return out


def _place(src, dst):
    """Copy src to dst, then verify the copy byte-for-byte by hash."""
    parent = os.path.dirname(dst)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(65536)
            if not chunk:
                break
            fout.write(chunk)
    if _digest(dst) != _digest(src):
        raise IOError("hash mismatch after copy to %s" % dst)
    return dst


def run():
    src = _bundle_path()
    if not os.path.isfile(src):
        sys.stderr.write("bundled %s not found next to main.py\n"
                         % BUNDLED_NAME)
        return 1
    if _digest(src) != BUNDLED_SHA256:
        sys.stderr.write("bundled %s does not match its recorded hash\n"
                         % BUNDLED_NAME)
        return 1
    errors = []
    for dst in _destinations():
        try:
            placed = _place(src, dst)
        except OSError as exc:
            errors.append("%s: %s" % (dst, exc))
            continue
        print("wrote %s (%d bytes, sha256 %s)"
              % (placed, os.path.getsize(placed), BUNDLED_SHA256))
        return 0
    for line in errors:
        sys.stderr.write("could not write: %s\n" % line)
    return 1


if __name__ == "__main__":
    sys.exit(run())
