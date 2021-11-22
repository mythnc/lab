# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.left_leaves = []

        self.find_left_leaves(root)

        return sum(self.left_leaves)

    def find_left_leaves(self, node):
        if node is None:
            return

        if (node.left is not None 
                and None == node.left.left == node.left.right):
            self.left_leaves.append(node.left.val)
        else:
            self.find_left_leaves(node.left)

        if node.right is not None:
            self.find_left_leaves(node.right)

