"""
using PDB to debug inside a test
"""

import pdb
import pytest

# pytest --pdb test_pytest_exp2.py
##
# h = help
# q = quit
# <variable> -> printing the value of the variable


def test_stuff():
    x = 5 * 5
    pdb.set_trace()  # Launch debugger -> it stops at this point
    assert x == 10
    # with q, exit from debugger


@pytest.fixture
def temp_dir():
    pass


# NOTE this does not work
#pytest test function using fixture
# def test_using_dir(temp_dir):
#     path = temp_dir.join("test.txt")


# pytest --help
# pytest -x -> stopping at first failure


# install plugins is easy, e.g.
# pip install pytest-xdist  -> allows multiple test runners in parallel
# e.g.
# pytest -n 4 -> 4 runners in parallel -> faster

