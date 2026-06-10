"""`test_my_module.py` testing MyClass from 'my_module.py'"""
from unittest.mock import Mock
from unittest.mock import patch

import pytest

from test_class_with_fixture import mocked_class, mocked_foo, mocked_bar
from my_module import MyClass

from my_module import MyClassWithIssueInInit
# # from my_loads import    MY_OBJ_WITH_ISSUE
from my_loading_module import bar


def test_mocking_foo(monkeypatch):
    """Mock 'my_module.foo' and test that it was called by the instance of
    MyClass.
    """
    my_mock = Mock()
    monkeypatch.setattr('my_module.foo', my_mock)

    MyClass().should_call_foo(1, 2, a=3, b=4)

    my_mock.assert_called_once_with(1, 2, a=3, b=4)


def test_mocking_foo2(monkeypatch):
    my_mock = Mock()
    monkeypatch.setattr("my_module.foo", my_mock)
    # monkeypatch.setattr("my_loading_module.bar", my_mock)

    # created = MyClassWithIssueInInit()


def test_mocking_foo3():
    with patch.object(MyClassWithIssueInInit, '__init__', lambda x: None):
        created = MyClassWithIssueInInit()
        #created.p = None


def test_mocking_foo4(mocked_class):
    #my_mock = Mock()
    print(mocked_class)


# def test_mocking_bar(mocked_bar):
#     my_mock = Mock()
#     monkeypatch.setattr('my_loading_module.bar', my_mock)
#     bar()


def test_mocking_foo_in_fixture(mocked_foo):
    """Using the 'mocked_foo' fixture to test that 'my_module.foo' was called
    by the instance of MyClass."""
    MyClass().should_call_foo(1, 2, a=3, b=4)

    mocked_foo.assert_called_once_with(1, 2, a=3, b=4)


# def test_mocking_bar_in_fixture(mocked_foo):
#     """Using the 'mocked_foo' fixture to test that 'my_module.foo' was called
#     by the instance of MyClass."""
#     MyClassWithIssueInInit().should_call_foo(1, 2, a=3, b=4)
#
#     mocked_foo.assert_called_once_with(1, 2, a=3, b=4)