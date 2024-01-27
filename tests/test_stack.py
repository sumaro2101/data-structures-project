import pytest
from src.stack import Node

@pytest.mark.node
def test_init_node():
    """Тесты инициализации объектов в стеке
    """  
      
    node1 = Node(33, None)
    node2 = Node(100, node1)
    node3 = Node('test', node2)
    
    assert node1.next_node == None
    assert node3.next_node.next_node.data == 33
    assert node2.data == 100
    assert node3.next_node.data == 100
    
    
@pytest.mark.stack
class TestStack:
    """Класс имеющий тесты связаные с методами Стэка
    """    
    
    def test_push1(self, stack):
        """Добавление объекта в стэк

        Args:
            stack (fixture): инициализация стэка
        """    
            
        stack.push('test')
        
        assert stack.top.data == 'test'
        
        
    def test_push2(self, stack):
        """Добавление еще одного объета в стек
        Тест что ссылка на предедущий объект в наличии

        Args:
            stack (fixture): инициализация стэка
        """  
             
        stack.push(11)
        
        assert stack.top.next_node.data == 'test'
        assert stack.top.next_node.next_node == None
        
        
    def test_push3(self, stack):
        """Добавление объектов
        Тест что ссылки на дальние объекты в наличии

        Args:
            stack (fixture): инициализация стэка
        """        
        
        stack.push('one')
        stack.push('two')
        stack.push('finaly')
        
        assert stack.top.next_node.next_node.data == 'one'
        assert stack.top.next_node.next_node.next_node.data == 11
    
    
    def test_pop(self, stack):
        """Удаление объекта

        Args:
            stack (fixture): инициализация стэка
        """   
             
        stack.pop()
        
        assert stack.top.data == "two"
        
        
    def test_pop_return(self, stack):
        """Тест возращения значения при удалении

        Args:
            stack (fixture): инициализация стэка
        """    
            
        assert stack.pop() == 'two'
        
        
    def test_pop_stack_none(self, stack):
        """Тест удаления последнего объекта
        top должен стать None

        Args:
            stack (fixture): инициализация стэка
        """        
        stack.pop()
        stack.pop()
        stack.pop()
        
        assert stack.top == None
        
    def test_pop_none(self, stack):
        """Тест возращаемого значение None при top None

        Args:
            stack (fixture): инициализация стэка
        """ 
               
        assert stack.pop() == None
        