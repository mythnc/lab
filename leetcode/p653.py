# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        elements = []
        self.traverse(root, elements)
        return self.is_exist(elements, k)

    def traverse(self, root, elements):
        if root.left is not None:
            self.traverse(root.left, elements)

        elements.append(root.val)

        if root.right is not None:
            self.traverse(root.right, elements)

    def is_exist(self, ary, k):
        for i in range(len(ary)):
            if k-ary[i] in ary[i+1:]:
                return True
        return False
