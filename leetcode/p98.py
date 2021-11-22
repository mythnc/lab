# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ary = []
        self.traverse(root, ary)
        return self.is_valid(ary)

    # inorder
    def traverse(self, root, ary):
        if root.left is not None:
            self.traverse(root.left, ary)

        ary.append(root.val)

        if root.right is not None:
            self.traverse(root.right, ary)

    def is_valid(self, ary):
        for i in range(1, len(ary)):
            if ary[i-1] >= ary[i]:
                return False
        return True
