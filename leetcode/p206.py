# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        pre_node = None
        node = head
        while node.next is not None:
            # head
            if pre_node is None:
                pre_node = node
                node = node.next
                pre_node.next = None
                continue
            next_node = node.next
            node.next = pre_node
            pre_node = node
            node = next_node
        node.next = pre_node
        return node
