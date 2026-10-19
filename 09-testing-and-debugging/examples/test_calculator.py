"""Run with:  pytest 09-testing-and-debugging/examples -v"""
import pytest

from calculator import Calculator, add, divide, is_even


# --- Simple tests --------------------------------------------------------
def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_divide():
    assert divide(10, 4) == 2.5


# --- Testing errors ------------------------------------------------------
def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError, match="divide by zero"):
        divide(1, 0)


# --- Parametrised test ---------------------------------------------------
@pytest.mark.parametrize("number, expected", [
    (0, True),
    (1, False),
    (2, True),
    (-4, True),
    (99, False),
])
def test_is_even(number, expected):
    assert is_even(number) == expected


# --- Fixtures ------------------------------------------------------------
@pytest.fixture
def calc():
    return Calculator()


def test_new_calculator_starts_at_zero(calc):
    assert calc.total == 0
    assert calc.history == []


def test_apply_operations(calc):
    calc.apply("+", 10)
    calc.apply("-", 3)
    assert calc.apply("*", 2) == 14
    assert len(calc.history) == 3


def test_unknown_operation(calc):
    with pytest.raises(ValueError):
        calc.apply("^", 2)
