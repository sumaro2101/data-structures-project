class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    top = None


    def push(self, data) -> None:
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        
        if self.top is None:
            self.top = Node(data, None)
            
        else:
            self.top = Node(data, self.top)
            
            
    def pop(self) -> (str|float|int|None):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        node = self.top
        
        if node == None:
            return None
        
        if node.next_node is None:
            self.top = None
            
        else:
            self.top = self.top.next_node
            return node.data
        