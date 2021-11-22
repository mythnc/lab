# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder: root, left, right
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, root, result):
        if root is None:
            return

        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)

