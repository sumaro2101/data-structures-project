import pytest

@pytest.mark.str
def test_queue_str_empty(queue):
    """Тест на пустой str

    Args:
        queue (fixture): инициализированный класс очереди
    """    
    
    assert str(queue) == ""
    
@pytest.mark.str
def test_queue_str(queue):
    """Тест str с полной очередью

    Args:
        queue (fixture): инициализированный класс очереди
    """    
    
    queue.enqueue("first")
    queue.enqueue("last")
    queue.enqueue("middle")
    
    assert str(queue) == "first\nlast\nmiddle"