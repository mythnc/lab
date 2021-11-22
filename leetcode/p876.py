from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = self.size(head)

        # find middle
        middle = (size + 1) // 2
        if size % 2 == 1:
            middle -= 1

        current = head
        for _ in range(middle):
            current = current.next
        return current

    def size(self, head):
        size = 1
        current = head
        while current.next is not None:
            current = current.next
            size += 1

        return size

