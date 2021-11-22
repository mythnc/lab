# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        # same as
        #if None in [l1, l2]:
        #    return l1 or l2


        n1 = l1
        n2 = l2
        if n1.val <= n2.val:
            result = n1
            n1 = n1.next
        else:
            result = n2
            n2 = n2.next

        n3 = result
        while n1 is not None and n2 is not None:
            if n1.val <= n2.val:
                n3.next = n1
                n1 = n1.next
            else:
                n3.next = n2
                n2 = n2.next
            n3 = n3.next

        if n1 is not None:
            n3.next = n1

        if n2 is not None:
            n3.next = n2

        return result
