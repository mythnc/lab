"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = [root]
        while (n := len(queue)) > 0:
            for i in range(1, n):
                queue[i-1].next = queue[i]
            queue[-1].next = None

            for i in range(n):
                if queue[i].left is not None:
                    queue.append(queue[i].left)
                if queue[i].right is not None:
                    queue.append(queue[i].right)

            queue = queue[n:]

        return root

