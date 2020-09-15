class Node:
    """The basic unit of the linked list."""

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self) -> str:
        return f"{self.value} -> {self.next_node}" \
            if self.next_node else str(self.value)
