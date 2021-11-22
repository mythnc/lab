# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes_bfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [root]
        count = 0
        while len(queue) > 0:
            node = queue.pop(0)
            count += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        return count

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return self.find(root, 1)

    def find(self, root, count):
        if root.left is None and root.right is None:
            return count

        if root.left is not None and root.right is None:
            return count * 2

        if root.left is not None and root.right is not None:
            return max(self.find(root.left, count * 2), self.find(root.right, count * 2 + 1))

