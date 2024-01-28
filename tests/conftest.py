import pytest

from src.stack import Stack, Node

@pytest.fixture(scope='class')
def stack():
    stack = Stack()
    return stack