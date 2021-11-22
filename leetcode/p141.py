# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        fast = head
        slow = head

        while fast.next is not None:
            fast = fast.next
            if fast.next is None:
                return False
            if fast is slow:
                return True
            fast = fast.next
            slow = slow.next
            if fast is slow:
                return True
