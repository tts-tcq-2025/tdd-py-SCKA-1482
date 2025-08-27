import pytest
from string_calculator import StringCalculator

calculator = StringCalculator()

def test_empty_string_returns_zero():
    assert calculator.add("") == 0

def test_single_number_returns_value():
    assert calculator.add("1") == 1

def test_two_numbers_comma_separated():
    assert calculator.add("1,2") == 3

def test_unknown_amount_of_numbers():
    assert calculator.add("1,2,3,4") == 10

def test_new_lines_between_numbers():
    assert calculator.add("1\n2,3") == 6

def test_custom_single_character_delimiter():
    assert calculator.add("//;\n1;2") == 3

def test_custom_multi_character_delimiter():
    assert calculator.add("//[***]\n1***2***3") == 6

def test_negative_numbers_throw_exception():
    with pytest.raises(ValueError) as excinfo:
        calculator.add("1,-2,3")
    assert "negatives not allowed: -2" == str(excinfo.value)

def test_multiple_negative_numbers_throw_exception():
    with pytest.raises(ValueError) as excinfo:
        calculator.add("1,-2,-3")
    assert "negatives not allowed: -2, -3" == str(excinfo.value)

def test_numbers_greater_than_1000_are_ignored():
    assert calculator.add("2,1001") == 2
