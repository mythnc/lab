# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = []

        if root is None:
            return None

        q.append(root)
        while len(q) > 0:
            result.append([n.val for n in q])
            new_q = []
            for n in q:
                if n.left is not None:
                    new_q.append(n.left)
                if n.right is not None:
                    new_q.append(n.right)
            q = new_q

        return result
