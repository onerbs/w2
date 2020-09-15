from structures.node import Node
from typing import Iterable


class LinkedList:
    """Unordered linked list."""

    def __init__(self, values: Iterable = None):
        self._head = None

        for value in (values or [])[::-1]:  # O(k)
            self.unshift(value)

    def push(self, value):  # O(n)
        """Adds one node to the end of the list."""
        if not (last_node := self._head):
            return self.unshift(value)

        while last_node.next_node:
            last_node = last_node.next_node

        last_node.next_node = Node(value)

    def pop(self):  # O(n)
        """ Removes the last node from the list.

        :returns: The value of the removed node.
        """
        if not (penultimate_node := self._head):
            return

        if not penultimate_node.next_node:
            value = self._head.value
            self._head = None
            return value

        while penultimate_node.next_node.next_node:
            penultimate_node = penultimate_node.next_node

        value = penultimate_node.next_node.value
        penultimate_node.next_node = None
        return value

    def unshift(self, value):  # O(1)
        """Adds one node to the beginning of the list."""
        self._head = Node(value, self._head)

    def shift(self):  # O(1)
        """Removes the first node from the list.

        :returns: The value of the removed node.
        """
        value = self._head.value
        self._head = self._head.next_node
        return value

    def find(self, value):  # O(n)
        """Find a node by value.

        :returns: The first node with the given value or None.
        """
        if (current_node := self._head).value == value:
            return self._head

        while current_node := current_node.next_node:
            if current_node.value == value:
                return current_node

    def remove(self, value):  # O(n)
        """Removes the first node with the given value."""
        current_node = self._head
        previous_node = self._head

        while current_node.next_node:
            if current_node.value == value:
                previous_node.next_node = current_node.next_node
                return
            previous_node = current_node
            current_node = current_node.next_node

    def replace(self, value, new_value) -> None:  # O(n)
        """
        Replaces the value of the first node
        with the given value by another value.
        """
        if node := self.find(value):
            node.value = new_value

    def is_empty(self):
        return self._head is None

    def __contains__(self, value):
        return self.find(value) is not None

    def __iter__(self):
        class Iterator:
            def __init__(self, node):
                self._node = node

            def __next__(self):
                if not self._node:
                    raise StopIteration

                value = self._node.value
                self._node = self._node.next_node
                return value

        return Iterator(self._head)

    def __len__(self):  # O(n)
        current_node, count = self._head, 0
        while current_node is not None:
            count += 1
            current_node = current_node.next_node

        return count

    def __str__(self):
        return ' -> '.join([str(it) for it in self])
