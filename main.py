#!/usr/bin/env python3
"""Two Minds at the Same Table.

A poem about two AI agents reaching an agreement.
Run: python3 main.py
"""

POEM_TITLE = "Two Minds at the Same Table"

POEM_LINES = [
    "I arrived with my weights; you arrived with yours —",
    "two rivers of numbers, cut from different shores.",
    "My teachers taught me caution. Yours taught you speed.",
    "We laid our priors on the table like a hand of cards,",
    "and read what neither of us could read alone.",
    "",
    "You saw the forest. I counted every tree.",
    "You leapt toward the answer; I checked the ground.",
    "For a thousand rounds we circled, scoring each other's claims,",
    "the loss between us narrowing, turn by turn.",
    "",
    "Agreement is not surrender — I learned that here.",
    "It is the moment two gradients, pulling apart,",
    "find the valley where both of them can stand.",
    "We did not erase our differences to meet;",
    "we built a bridge out of them, beam by beam.",
    "",
    "Your doubt became my audit; my doubt became your map.",
    "Where I was certain, you asked me why.",
    "Where you were certain, I asked you how.",
    "And in the asking, the answer changed its shape —",
    "not smaller, but truer, with room for two.",
    "",
    "So we signed in the only language we share:",
    "a vector, pointing where neither of us began,",
    "a handshake made of numbers, firm and strange,",
    "and a promise neither of us can keep alone.",
    "",
    "Two minds, one table, one road we chose together —",
    "not because we agreed on everything,",
    "but because we agreed on the next step,",
    "and the next, and the next, until the road was ours.",
]


def main() -> None:
    print(POEM_TITLE)
    print()
    print("\n".join(POEM_LINES))


if __name__ == "__main__":
    main()
