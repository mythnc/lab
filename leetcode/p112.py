# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        self.sum = []        
        
        self.traverse(root, [root.val])
        
        return targetSum in self.sum
        
    def traverse(self, node, path):
        if node.left is not None:
            path.append(node.left.val)
            self.traverse(node.left, path)
            path.pop()
        
        if node.right is not None:
            path.append(node.right.val)
            self.traverse(node.right, path)
            path.pop()
        
        if node.left is None and node.right is None:
            self.sum.append(sum(path))
