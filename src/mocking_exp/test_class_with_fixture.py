from unittest.mock import Mock, patch
import pytest

from my_module import MyClass, MyClassWithIssueInInit


@pytest.fixture
def mocked_foo(monkeypatch):
    """Fixture that will mock 'my_module.foo' and return the mock."""
    my_mock = Mock()
    monkeypatch.setattr('my_module.foo', my_mock)
    return my_mock


@pytest.fixture
def mocked_class(monkeypatch):
    my_mock = Mock()
    with patch.object(MyClassWithIssueInInit, "__init__", lambda x: None):
        created = MyClassWithIssueInInit()
    return created


@pytest.fixture
def mocked_bar(monkeypatch):
    my_mock = Mock()
    monkeypatch.setattr('my_loading_module.bar', my_mock)
    return my_mock