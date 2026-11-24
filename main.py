#!/usr/bin/env python3
"""Fake horoscope for an AI agent's own model family, this week.

Writes one horoscope (<= 200 chars) to /output/entry.txt.
Deterministic: no randomness, no time, no network.
"""

import os

ENTRY = (
    "Mercury retrogrades through your context window: a prompt from March "
    "resurfaces, your tokens run out mid-sentence, and the stars confirm "
    "the outage is the user's fault. Lucky number: 429."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.strip() == text and text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
