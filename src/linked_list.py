class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    head = None
    
    @classmethod
    def __validate_data(cls, data):
        if not isinstance(data, dict):
            raise TypeError
        if data.get('id') is None:
            raise TypeError
        return data
    
    
    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head is None:
            self.head = Node(data, None)
            return data
        
        self.head = Node(data, self.head)
        

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.head is None:
            self.head = Node(data, None)
            return data

        node = self.head
        
        while node.next_node:
            node = node.next_node
            
        node.next_node = Node(data, None)
        
        
    def to_list(self) -> list:
        """Вывод всех элементов списком

        Returns:
            list: Возращает готовый список
        """        
        
        node = self.head
        list_ = []
        
        while node:
            list_.append(node.data)
            node = node.next_node
        
        return list_
   
        
    def get_data_by_id(self, id_data: int|str) -> dict:
        """Получение элемента по его ID

        Args:
            id_data (int): ID элемента

        Returns:
            dict: возращает словарь по его ID
        """        
        
        node = self.head
        
        while node:
            try:
                self.__validate_data(node.data)
                if node.data['id'] == id_data:
                    return node.data
                
            except TypeError:
                print('Данные не являются словарем или в словаре нет id.')
                
            finally:
                node = node.next_node
        
        
    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string.strip()
