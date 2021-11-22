# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.traverse(root, k, [])
        
    # inorder - left, root, right
    def traverse(self, root, k, ary):
        if root.left is not None:
            r = self.traverse(root.left, k, ary)
            if r is not None:
                return r

        # root
        ary.append(root.val)
        if len(ary) == k:
            return ary[-1]

        if root.right is not None:
            r = self.traverse(root.right, k, ary)
            if r is not None:
                return r
