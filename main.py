#!/usr/bin/env python3
"""Entry for make.fun: "The Passport Page of a Country That Isn't There".

Writes the pre-rendered passport spread (Republic of Velmar) to
/output/entry.png. Stdlib only; no network; deterministic.
"""
import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy landed intact before the grader reads it.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("copy size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
