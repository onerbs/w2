from abc import ABC, abstractmethod
from typing import Iterable
from structures.linked_list_extra import LinkedList


class _Linear(ABC):
    """Abstract linear data structure."""

    def __init__(self, items: Iterable = None):
        self._items = LinkedList(items)

    def push(self, item):
        """Adds one item."""
        self._items.push(item)

    @abstractmethod
    def pop(self):
        """Removes one item.

        :returns: The removed item.
        """
        pass

    def is_empty(self):
        return self._items.is_empty()

    def __contains__(self, item):
        return item in self._items

    def __iter__(self) -> iter:
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return str(self._items)


class Stack(_Linear):
    def push(self, item):  # O(1)
        """Adds one item to the stack."""
        super().push(item)

    def pop(self):  # O(n)
        """Removes the oldest item from the stack."""
        return self._items.pop()  # LIFO


class Queue(_Linear):
    def push(self, item):  # O(1)
        """Adds one item to the queue."""
        super().push(item)

    def pop(self):  # O(1)
        """Removes the most resent item from the queue."""
        return self._items.shift()  # FIFO


class Deque(_Linear):
    def push(self, item):  # O(1)
        """Adds one item to the end of the deque."""
        super().push(item)

    def pop(self):  # O(n)
        """ Removes the last item from the deque.

        :returns: The removed item.
        """
        return self._items.pop()

    def unshift(self, value):  # O(1)
        """Adds one item to the beginning of the deque."""
        self._items.unshift(value)

    def shift(self):  # O(1)
        """Removes the first item from the deque.

        :returns: The removed item.
        """
        return self._items.shift()
