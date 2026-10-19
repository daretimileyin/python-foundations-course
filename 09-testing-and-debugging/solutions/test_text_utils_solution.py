import pytest

from text_utils import is_palindrome, most_common_letter, truncate, word_count


def test_word_count_simple_sentence():
    assert word_count("hello big world") == 3


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_extra_whitespace():
    assert word_count("  lots   of\tspace\n ") == 3


@pytest.mark.parametrize("text, expected", [
    ("racecar", True),
    ("Racecar", True),
    ("A man, a plan, a canal: Panama", True),
    ("python", False),
    ("", True),
    ("a", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


def test_truncate_short_text_unchanged():
    assert truncate("hi", 10) == "hi"


def test_truncate_exact_length_unchanged():
    assert truncate("hello", 5) == "hello"


def test_truncate_long_text():
    assert truncate("hello world", 8) == "hello..."


def test_truncate_result_length():
    assert len(truncate("a" * 100, 20)) == 20


def test_truncate_minimum_length():
    assert truncate("hello", 3) == "..."


def test_truncate_too_small_raises():
    with pytest.raises(ValueError):
        truncate("hello", 2)


def test_most_common_letter():
    assert most_common_letter("banana") == "a"


def test_most_common_letter_ignores_case_and_symbols():
    assert most_common_letter("B! b? a") == "b"


def test_most_common_letter_tie_is_alphabetical():
    assert most_common_letter("abab") == "a"


def test_most_common_letter_no_letters():
    assert most_common_letter("123 !!") is None
