import json
class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.head is None:
            self.head = Node(data, None)
            return data
            
        if self.tail is None:
            self.tail = Node(data, None)
            self.head.next_node = self.tail
            return data
        
        elem = self.head
        
        while elem.next_node:
            elem = elem.next_node
        
        elem.next_node = Node(data, None)
        self.tail = elem.next_node
        

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        
        if self.tail is None:
            item_return = self.head.data
            self.head = None
            return item_return
        
        if self.head.next_node == self.tail:
            item_return = self.tail.data
            self.tail = None
            self.head.next_node = None
            return item_return
        
        item_return = self.head
        prev_item = self.head
        
        while item_return.next_node:
            prev_item = item_return
            item_return = item_return.next_node
            if not item_return.next_node:
                self.tail = prev_item
                self.tail.next_node = None
                return item_return.data
            

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if self.head is None:
            return ""
        result = []
        elem = self.head
        while elem.next_node:
            result.append(elem.data)
            elem = elem.next_node
        result.append(elem.data)
        
        return '\n'.join(result)
