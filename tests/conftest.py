import pytest

from src.stack import Stack, Node
from src.queue import Queue

@pytest.fixture(scope='class')
def stack():
    stack = Stack()
    return stack

@pytest.fixture(scope='class')
def queue():
    queue = Queue()
    return queue