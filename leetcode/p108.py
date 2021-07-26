# 108. Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        mid_i = n // 2
        left_nodes = nums[:mid_i]
        val = nums[mid_i]
        right_nodes = nums[mid_i+1:]
        
        return TreeNode(val, self.sortedArrayToBST(left_nodes), self.sortedArrayToBST(right_nodes))
  
