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
        
        
    def test_lin_list_to_list(self, linked_list):
        """Тест вывода списка элементов в виде списка

        Args:
            linked_list (fixture): инициализированный односвязный список
        """  
        
        linked_list.insert_at_end({'id': 'test_two'})
        linked_list.insert_beginning([1, 2, 3, 4])
        linked_list.insert_beginning({'not_id': 10})
        
        assert linked_list.to_list() == [{'not_id': 10}, [1, 2, 3, 4], {'id': 'test'}, {'id': 'test_two'}]
        
        
    def test_lin_list_searchID(self, linked_list):
        """Тест поиска по ID

        Args:
            linked_list (fixture): инициализированный односвязный список
        """ 
        
        assert linked_list.get_data_by_id('test') == {'id': 'test'}
        