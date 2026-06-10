"""
fixtures
"""

import os
import pytest

from test_pytest_exp1 import str_to_bool

CURR_DIR = os.path.abspath(os.path.dirname(__file__))


def write_integer(my_string, path):
    with open(path, "w") as f:
        try:
            f.write(str(str_to_bool(my_string)))
        except RuntimeError:
            f.write(0)


class TestWriteBooleans:
    test_value_fn = "test_value.txt"
    test_value_path = f"{CURR_DIR}/tmp/{test_value_fn}"

    def setup_method(self):
        if os.path.exists(TestWriteBooleans.test_value_path):
            os.remove(TestWriteBooleans.test_value_path)

    def test_write_yes(self):
        write_integer("yes", TestWriteBooleans.test_value_path)
        with open(TestWriteBooleans.test_value_path, "r") as f:
            value = f.read()
        assert value == "True"

    def test_write_n(self):
        write_integer("n", TestWriteBooleans.test_value_path)
        with open(TestWriteBooleans.test_value_path, "r") as f:
            value = f.read()
        assert value == "False"


class TestFixtures:

    @pytest.mark.parametrize("tmpdir", [CURR_DIR, "tmp", "not-existing"])
    def test_write_yes(self, tmpdir):
        path = str(os.path.join(tmpdir, TestWriteBooleans.test_value_fn))
        print(f"The path from tmpdir fixture is: {path}")
        write_integer("yes", path)
        with open(path, "r") as f:
            value = f.read()
        assert value == "True"