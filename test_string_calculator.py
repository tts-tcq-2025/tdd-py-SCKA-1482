import pytest
from string_calculator import StringCalculator

@pytest.fixture
def calc():
    return StringCalculator()

def test_empty_string_returns_zero(calc):
    assert calc.add("") == 0

def test_single_number_returns_that_number(calc):
    assert calc.add("1") == 1

def test_two_numbers_comma_separated(calc):
    assert calc.add("1,2") == 3

def test_unknown_amount_of_numbers(calc):
    assert calc.add("1,2,3,4") == 10

def test_new_lines_between_numbers(calc):
    assert calc.add("1\n2,3") == 6

def test_custom_single_character_delimiter(calc):
    assert calc.add("//;\n1;2") == 3

def test_custom_multi_character_delimiter(calc):
    assert calc.add("//[***]\n1***2***3") == 6

def test_negative_number_throws_exception(calc):
    with pytest.raises(ValueError) as excinfo:
        calc.add("1,-2,3")
    assert str(excinfo.value) == "negatives not allowed: -2"

def test_multiple_negative_numbers_throw_exception(calc):
    with pytest.raises(ValueError) as excinfo:
        calc.add("1,-2,-3")
    assert str(excinfo.value) == "negatives not allowed: -2, -3"

def test_numbers_greater_than_1000_are_ignored(calc):
    assert calc.add("2,1001") == 2
