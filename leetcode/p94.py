# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder: left, root, right
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root is None:
            return

        self.traverse(root.left, result)
        result.append(root.val)
        self.traverse(root.right, result)
 
