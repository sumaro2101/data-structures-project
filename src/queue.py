import json
from typing import Any

class Node:
    """Класс для узла очереди"""

    def __init__(self, data: Any, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self, head: Any=None, tail: Any=None):
        self.head = head
        self.tail = tail
    
    
    def enqueue(self, data: Any) -> None:
        """
        Метод для добавления элемента в очередь

        Если голова None - элемент сохранить в голову
        Если хвост None - элемент сохранить в хвост
    
        
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
        

    def dequeue(self) -> Any:
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента
        
        Если хвост None - Голова None
        Если следующий элемент Головы равен Хвосту - Хвост None


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
     
    @staticmethod      
    def list_items(ent_elem) -> list:
        """Создает список элементов списка

        Returns:
            list: Возращает список элементов
        """    
            
        result = []
        elem = ent_elem
        
        while elem.next_node:
            result.append(elem.data)
            elem = elem.next_node
        result.append(elem.data)
        
        return result


    def __str__(self) -> str:
        """Магический метод для строкового представления объекта"""
        
        if self.head is None:
            return ""
        
        return '\n'.join(self.list_items(self.head))
