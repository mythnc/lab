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

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False

        return self.traverse(root, targetSum)

    def traverse(self, root, targetSum, sum_=None):
        if sum_ is None:
            sum_ = root.val
        else:
            sum_ += root.val

        if root.left is None and root.right is None:
            return sum_ == targetSum

        if root.left is None:
            return self.traverse(root.right, targetSum, sum_)

        if root.right is None:
            return self.traverse(root.left, targetSum, sum_)

        return (self.traverse(root.left, targetSum, sum_)
            or self.traverse(root.right, targetSum, sum_))
