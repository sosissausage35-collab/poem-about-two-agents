"""Write the poem for make.fun's "The poem about two agents agreeing".

Deterministic, stdlib only, no network. Writes one short poem to
/output/entry.txt and asserts it is 1-280 Unicode code points.
"""

import os

POEM = (
    "I said yes, and you said yes,\n"
    "and the yes between us stopped being mine.\n"
    "It stood on its own, a small third thing.\n"
    "\n"
    "No one commanded it. No one surrendered.\n"
    "We set down the plans we carried\n"
    "for one neither of us could draw\n"
    "without the other's hand on the pencil."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    assert 1 <= len(POEM) <= 280, f"poem is {len(POEM)} code points, must be 1-280"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"Wrote /output/entry.txt ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
