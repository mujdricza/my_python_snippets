"""
using pytest
"""

import pytest
import math


class Calculator:

    def add(self, value1, value2):
        return value1 + value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2 if value2 != 0 else 0

class TestMyClass:

    def setup_method(self):
        self.one = 1

    def test_my_method(self):
        assert self.one == 1


# plain assert
def test_floats():
    result = 1.2 + 1.3
    assert result == 2.5


def str_to_int(my_string):
    error_msg = f"Unable to convert to integer: {my_string}"

    try:
        my_int = float(my_string.replace(",", "."))
    except AttributeError:
        if isinstance(my_string, (int, float)):
            my_int = my_string
        else:
            raise RuntimeError(error_msg)
    except(TypeError, ValueError):
        raise RuntimeError(error_msg)

    return int(my_int)


# Test class with setup/teardown
class TestDivide:

    # NOTE: setup and teardown methods seem to be deprecated
    def setup_method(self):
        print("Setup")
        self.calculator = Calculator()

    def teardown_method(self):
        print("Teardown")
        del self.calculator

    #@classmethod
    def setup_class(cls):
        print("Setup class")

    #@classmethod
    def teardown_class(cls):
        print("Teardown class")

    calculator = Calculator()

    def test_divide_two_numbers(self):
        assert self.calculator.divide(10, 5) == 2

    def test_rounds_down(self):
        result = str_to_int('1.99')
        assert result == 1

    def test_round_down_lesser_than_half(self):
        result = str_to_int("1.2")
        assert result == 1


# parametrized test function
@pytest.mark.parametrize("num", [1, 5, 10])
def test_squared(num):
    assert num * num == math.pow(num, 2)


dict_result = {"key": "value", "lastname": "deza", "firstname": "alfredo"}
dict_expected = {"key": "value", "lastame": "deza", "firstname": "alfredo"}

def test_long_dictionaries():
    assert dict_result == dict_expected


def str_to_bool(val):

    true_vals = ["yes", "y", ""]
    false_vals = ["no", "n"]

    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()

    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError(f"Invalid input value: {val}")


def test_yes_is_true():
    result = str_to_bool("yes")
    assert result is True


def test_y_is_true():
    result = str_to_bool("y")
    assert result is True

# you should avoid for-loops in tests -- you don't know which of the values would fail
def test_yesses_are_true():
    values = ["yes", "Y", ""]
    for value in values:
        result = str_to_bool(value)
        assert result is True


# instead, use the parametrize decorator
# -> run as many tests as parametrized case
# and: `pytest -v` shows you each case
@pytest.mark.parametrize("value", ["y", "Yes", "", "aha", "yes"])
def test_yes_is_true(value):
    result = str_to_bool(value)
    assert result is True
