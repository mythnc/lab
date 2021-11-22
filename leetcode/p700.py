# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        try:
            if (node_val := root.val) == val:
                return root
            elif val > node_val:
                return self.searchBST(root.right, val)
            elif val < node_val:
                return self.searchBST(root.left, val)
        except AttributeError:
            return None
