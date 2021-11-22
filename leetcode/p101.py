# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.equals(root.left, root.right)

    def equals(self, left_node, right_node):
        try:
            if left_node.val != right_node.val:
                return False
        except AttributeError:
            return left_node == right_node == None

        return (self.equals(left_node.left, right_node.right)
                and self.equals(left_node.right, right_node.left))
