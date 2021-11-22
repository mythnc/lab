# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.path = []
        self.sum = 0
        
        # DFS
        self.dfs(root)
        return self.sum


    def dfs(self, root):
        self.path.append(str(root.val))

        # terminal cond
        if root.left is None and root.right is None:
            self.sum += int("".join(self.path))

        if root.left is not None:
            self.dfs(root.left)

        if root.right is not None:
            self.dfs(root.right)

        self.path.pop()
