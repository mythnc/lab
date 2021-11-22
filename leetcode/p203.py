# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        while head is not None and head.val == val:
            head = head.next
            
        if head is None:
            return None
                
        current = head
        while current.next is not None:
            while current.next.val == val:
                if current.next.next is not None:
                    current.next = current.next.next
                else:
                    current.next = None
                    break
            current = current.next
            if current is None:
                break
            
        return head
