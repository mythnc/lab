# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        d = 0
        return self.find_depth(root, d)

    def find_depth(self, root, d):
        if root is None:
            return d

        # return 1 + max(self.find_depth(root.left, d), self.find_depth(root.right, d))
        # then we could use original method directly
        return max(self.find_depth(root.left, d+1), self.find_depth(root.right, d+1))
