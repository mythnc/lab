# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    map_ = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        if root in self.map_:
            return self.map_[root]

        if root is None:
            return 0

        # cond1: no self + children
        cond1_sum = 0
        if (left_node := root.left) is not None:
            self.map_[left_node] = self.rob(left_node)
            cond1_sum += self.map_[left_node]
        if (right_node := root.right) is not None:
            self.map_[right_node] = self.rob(right_node)
            cond1_sum += self.map_[right_node]

        # cond2: self + grandchildren
        cond2_sum = root.val
        if left_node is not None:
            self.map_[left_node.left] = self.rob(left_node.left)
            self.map_[left_node.right] = self.rob(left_node.right)
            cond2_sum += self.map_[left_node.left] + self.map_[left_node.right]

        if right_node is not None:
            self.map_[right_node.left] = self.rob(right_node.left)
            self.map_[right_node.right] = self.rob(right_node.right)
            cond2_sum += self.map_[right_node.left] + self.map_[right_node.right]

        return max(cond1_sum, cond2_sum)
