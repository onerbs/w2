from structures.linked_list import LinkedList as _LinkedList
from structures.node import Node
from typing import Iterable


class LinkedList(_LinkedList):
    """Unordered linked list."""

    def __init__(self, values: Iterable = None):
        self._head = None
        self._tail = None

        for value in (values or []):
            self.push(value)

    def push(self, value):  # O(1)
        if self._head is None:
            return self.unshift(value)

        _node = self._tail or self._head
        _node.next_node = Node(value)
        self._tail = _node.next_node

    def unshift(self, value):  # O(1)
        super().unshift(value)

        if self._tail is None:
            self._tail = self._head.next_node
