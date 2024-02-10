import pytest

from src.stack import Stack
from src.queue import Queue
from src.linked_list import LinkedList

@pytest.fixture(scope='class')
def stack():
    stack = Stack()
    return stack

@pytest.fixture(scope='class')
def queue():
    queue = Queue()
    return queue

@pytest.fixture(scope='class')
def linked_list():
    list_ = LinkedList()
    return list_