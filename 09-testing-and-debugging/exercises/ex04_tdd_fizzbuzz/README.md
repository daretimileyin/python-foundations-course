# ⭐⭐⭐ Exercise 4 – TDD: Roman Numerals

Build `to_roman(n)` **test-first**. It converts an integer (1–3999) to a Roman numeral string.

| n | roman |
|---|-------|
| 1 | I |
| 4 | IV |
| 9 | IX |
| 14 | XIV |
| 40 | XL |
| 90 | XC |
| 400 | CD |
| 1994 | MCMXCIV |
| 2026 | MMXXVI |

## The rules of TDD
1. 🔴 Write ONE small test in `test_roman.py` (start with `to_roman(1) == "I"`). Run pytest and watch it **fail**.
2. 🟢 Write the **simplest** code in `roman.py` to make it pass, even if it feels silly.
3. 🔵 Refactor if needed. Run the tests again.
4. Repeat with the next test (2 → "II", 4 → "IV", 5 → "V"...)

Finally, add a test that `to_roman(0)` and `to_roman(4000)` raise `ValueError`.

**Commit after each green step.** Your commit history should tell the TDD story!

Create the two files yourself: `roman.py` and `test_roman.py`.
