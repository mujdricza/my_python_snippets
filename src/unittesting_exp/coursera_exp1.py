"""
    Testing - Validating code behavior through automated scripts to check for correctness and catch issues.

    Unit Test - Testing isolated chunks of code like functions or classes.

    Test Function - An isolated test wrapped in a Python function.

    Test Class - A class that contains related test methods.

    Assertion - Boolean checks in test code to verify values match expectations.

    Fixture - Shared test data or state managed by the testing framework.
"""

class Calculator:

    def add(self, value1, value2):
        return value1 + value2

    def multiply(self, value1, value2):
        return value1 * value2



# Using assertions in a test function
def test_capitalize():
    assert "hello".capitalize() == "Hello"


# Class with two related test methods
class TestCalculator:

    def test_add(self):
        calculator = Calculator()
        assert calculator.add(2, 2) == 4

    def test_multiply(self):
        calculator = Calculator()
        assert calculator.multiply(3, 5) == 15


# Test function using pytest fixture for temp data
import pytest


@pytest.fixture
def input_value():
    return 10


def test_stuff(input_value):
    assert input_value == 10