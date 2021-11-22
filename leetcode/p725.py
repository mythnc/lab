# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        node = head
        # get len of nodes
        while node is not None:
            node = node.next
            n += 1

        if n == 0:
            return [None for _ in range(k)]

        q = n // k
        r = n % k
        result = []
        node = head
        while k > 0:
            result.append(node)

            times = q if r > 0 else q-1
            for _ in range(times):
                if node is None:
                    break
                node = node.next

            if node is not None:
                next_node = node.next
                node.next = None
                node = next_node

            k -= 1
            if r > 0:
                n -= (q + 1)
                q = n // k
                r = n % k

        return result
