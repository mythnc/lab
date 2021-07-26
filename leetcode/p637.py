# https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q = []
        q.append(root)
        ans = []
        precision = 10**5
        while len(q) > 0:
            avg = sum((node.val for node in q)) / len(q)
            ans.append(int(avg * precision) / precision)

            nodes = [node for node in q]
            q = []
            for node in nodes:
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
    
        return ans
