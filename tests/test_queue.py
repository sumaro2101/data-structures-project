import pytest

@pytest.mark.queue
class TestQueue:
    """Тесты очереди
    """    
    
    def test_enqueue_elem_head(self, queue):
        """Тест инициализации "головы"

        Args:
            queue (fixture): инициализированный класс очереди
        """ 
               
        queue.enqueue("first")
        
        assert queue.head.data == "first"
        
        
    def test_enqueue_elem_tail(self, queue):
        """Тест инициализации "Хвоста"

        Args:
            queue (fixture): инициализированный класс очереди
        """  
              
        queue.enqueue("last")
        
        assert queue.tail.data == "last" and queue.head.next_node.data == "last"
        
        
    def test_enqueue_elem(self, queue):
        """Тест инициализации элемента в полноценную очередь

        Args:
            queue (fixture): инициализированный класс очереди
        """    
            
        queue.enqueue("middle")
        
        assert queue.tail.data == "middle" and queue.head.next_node.next_node.data == "middle"
        
        
    def test_dequeue(self, queue):
        """Тест удаления элемента в полной очереди

        Args:
            queue (fixture): инициализированный класс очереди
        """        
        
        assert queue.dequeue() == "middle"
        
        
    def test_dequeue_tail(self, queue):
        """Тест удаления "Хвоста"

        Args:
            queue (fixture): инициализированный класс очереди
        """   
             
        queue.dequeue()
        assert queue.tail is None and queue.head.next_node is None
        
        
    def test_dequeue_head(self, queue):
        """Тест удаления "Головы"

        Args:
            queue (fixture): инициализированный класс очереди
        """ 
               
        queue.dequeue()
        
        assert queue.head is None