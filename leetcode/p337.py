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

        sum_ = root.val
        if (left_node := root.left) is not None:
            sum_ += self.rob(left_node.left) + self.rob(left_node.right)

        if (right_node := root.right) is not None:
            sum_ += self.rob(right_node.left) + self.rob(right_node.right)
    
        # cond1: no self + children
        # cond2: self + grandchildren
        self.map_[root] = max(self.rob(root.left) + self.rob(root.right) , sum_)
        return self.map_[root]
