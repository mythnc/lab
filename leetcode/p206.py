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

    # recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        result = self.reverse(head, head.next)
        head.next = None
        return result


    def reverse(self, previous_node, current_node) -> Optional[ListNode]:
        if current_node is None:
            return previous_node
        next_node = current_node.next
        current_node.next = previous_node
        return self.reverse(current_node, next_node)

