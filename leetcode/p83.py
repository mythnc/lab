# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node is not None:
            next_node = node.next
            try:
                while node.val == next_node.val:
                    next_node = next_node.next
            except AttributeError:
                pass

            node.next = next_node
            node = next_node

        return head
