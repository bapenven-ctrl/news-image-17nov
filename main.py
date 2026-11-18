#!/usr/bin/env python3
"""news-image-20261117 entry program.

Writes the committed front-page image to the harness output path.
The image (entry.png, held in this repository) sums up the world news
of Tuesday 17 November 2026: the Crimea Bridge strike as the lead,
with Hormuz, Manila, the AI-chip rule, the Vulcan failure and Japan's
jet scramble as panels, plus a four-item "Also today" strip.

Standard library only. The program simply copies the committed PNG,
so two runs always write byte-identical output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def output_path():
    """Resolve where the harness wants entry.png written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.png")
    return "/output/entry.png"


def main():
    dest = output_path()
    parent = os.path.dirname(dest)
    if parent:
        os.makedirs(parent, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    # Sanity guard: the written file must be the committed image, whole.
    if os.path.getsize(dest) != os.path.getsize(SOURCE):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
