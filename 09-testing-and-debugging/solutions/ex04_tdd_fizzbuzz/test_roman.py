import pytest

from roman import to_roman


@pytest.mark.parametrize("n, expected", [
    (1, "I"), (2, "II"), (4, "IV"), (5, "V"), (9, "IX"), (14, "XIV"),
    (40, "XL"), (90, "XC"), (400, "CD"), (1994, "MCMXCIV"), (2026, "MMXXVI"),
    (3999, "MMMCMXCIX"),
])
def test_to_roman(n, expected):
    assert to_roman(n) == expected


@pytest.mark.parametrize("n", [0, -1, 4000])
def test_out_of_range_raises(n):
    with pytest.raises(ValueError):
        to_roman(n)
