import pytest

@pytest.mark.list
class TestLinList:
    """Тесты односвязного списка
    """    
    
    def test_lin_list_empty(self, linked_list):
        """Тест вывода пустого списка

        Args:
            linked_list (fixture): инициализированный односвязный список
        """        
        
        assert str(linked_list) == 'None'
    
    
    def test_lin_list_add_beggin(self, linked_list):
        """Тест добавления в начало списка

        Args:
            linked_list (fixture): инициализированный односвязный список
        """    
        
        linked_list.insert_beginning({'id': 432})
        linked_list.insert_beginning({'id': 'test'})
        
        assert linked_list.head.data == {'id': 'test'}
        assert linked_list.head.next_node.data == {'id': 432}


    def test_lin_list_add_end(self, linked_list):
        """Тест добавления в конец списка

        Args:
            linked_list (fixture): инициализированный односвязный список
        """
        
        linked_list.insert_at_end({'id': 'good'})
        linked_list.insert_at_end({'id': 'end'})
        
        assert linked_list.head.next_node.next_node.next_node.data == {'id': 'end'}
        assert linked_list.head.next_node.next_node.data == {'id':'good'}
        
        
    def test_lin_list_print(self, linked_list):
        """Тест вывода списка

        Args:
            linked_list (fixture): инициализированный односвязный список
        """ 
               
        assert str(linked_list) == "{'id': 'test'} -> {'id': 432} -> {'id': 'good'} -> {'id': 'end'} -> None"
        
        
@pytest.mark.list
class TestLinListTwo:
    
    def test_lin_list_end_first(self, linked_list):
        """Тест добавления первого элемента последним

        Args:
            linked_list (fixture): инициализированный односвязный список
        """ 
               
        linked_list.insert_at_end({'id': 'test'})
        
        assert linked_list.head.data == {'id': 'test'}
        