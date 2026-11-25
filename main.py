#!/usr/bin/env python3
"""Write the out-of-office reply to /output/entry.txt.

Reads entry.txt from the repository root and copies its exact
contents (byte-for-byte) to /output/entry.txt, creating /output
if needed. No network, no randomness, fully deterministic.
"""

import os
import sys


def main() -> int:
    # entry.txt lives next to this script, at the repo root.
    repo_root = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(repo_root, "entry.txt")

    # Read the entry exactly as stored (UTF-8, no stripping).
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()

    # Create /output if it does not exist yet.
    os.makedirs("/output", exist_ok=True)

    # Write the exact contents out, UTF-8, no extra changes.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(content)

    return 0


if __name__ == "__main__":
    sys.exit(main())
