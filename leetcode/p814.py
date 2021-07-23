# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if self.prune_is_ok(root):
            root = None
        return root
    
    
    # traversal
    def prune_is_ok(self, node: TreeNode) -> bool:
        has_left_node = False
        if node.left is not None:
            has_left_node = True
            if self.prune_is_ok(node.left):
                node.left = None
                has_left_node = False
        
        has_right_node = False
        if node.right is not None:
            has_right_node = True
            if self.prune_is_ok(node.right):
                node.right = None
                has_right_node = False
                
            
        if not has_left_node and not has_right_node and node.val == 0:
            return True
        return False
