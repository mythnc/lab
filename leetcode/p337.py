# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.map_ = {}
        return self.dp(root, 1)

    def dp(self, root, index):
        if index in self.map_:
            return self.map_[index]

        if root is None:
            return 0

        # cond1: no self + children
        left_node_index = index * 2
        right_node_index = index * 2 + 1
        self.map_[left_node_index] = self.dp(root.left, left_node_index)
        self.map_[right_node_index] = self.dp(root.right, right_node_index)
        cond1_sum = self.map_[left_node_index] + self.map_[right_node_index]

        # cond2: self + grandchildren
        cond2_sum = root.val
        if (left_node := root.left) is not None:
            left_node_index_in_left_node = left_node_index * 2
            self.map_[left_node_index_in_left_node] = self.dp(left_node.left, left_node_index_in_left_node)

            right_node_index_in_left_node = left_node_index * 2 + 1
            self.map_[right_node_index_in_left_node] = self.dp(left_node.right, right_node_index_in_left_node)

            cond2_sum += self.map_[left_node_index_in_left_node] + self.map_[right_node_index_in_left_node]

        if (right_node := root.right) is not None:
            left_node_index_in_right_node = right_node_index * 2
            self.map_[left_node_index_in_right_node] = self.dp(right_node.left, left_node_index_in_right_node)

            right_node_index_in_right_node = right_node_index * 2 + 1
            self.map_[right_node_index_in_right_node] = self.dp(right_node.right, right_node_index_in_right_node)

            cond2_sum += self.map_[left_node_index_in_right_node] + self.map_[right_node_index_in_right_node]

        return max(cond1_sum, cond2_sum)
