"""One Star, Written in Sap — a one-line 1-star review, under 280 characters.

The joke: a houseplant reviews its human the way a guest reviews a bad
Airbnb host — watered on a schedule without anyone checking the soil, and
moved three times for "better light" that turned out to be radiators.
"""

import os

ENTRY = "One star. The host waters on a schedule, never once checks the soil, and has moved me three times for 'better light' \u2014 all three spots were radiators. Would not photosynthesise here again."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
