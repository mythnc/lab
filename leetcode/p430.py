"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head

        current = head
        while current is not None:
            if current.child is None:
                current = current.next
                continue

            # change child to next
            old_next = current.next
            child_node = current.child
            current.next = child_node
            child_node.prev = current
            current.child = None

            if old_next is None:
                continue

            # find last node in child layer
            while child_node.next is not None:
                child_node = child_node.next

            child_node.next = old_next
            old_next.prev = child_node

            current = current.next

        return head
