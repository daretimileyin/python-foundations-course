"""
⭐⭐ Exercise 2 – Write the tests!

Write AT LEAST 12 tests for text_utils.py, covering:
  - normal cases
  - edge cases (empty strings, single characters, exact boundaries)
  - truncate raising ValueError (use pytest.raises)
  - at least one @pytest.mark.parametrize test

Run with:  pytest 09-testing-and-debugging/exercises -v
"""
import pytest

from text_utils import is_palindrome, most_common_letter, truncate, word_count


def test_word_count_simple_sentence():
    assert word_count("hello big world") == 3


# TODO: write more tests below 👇
