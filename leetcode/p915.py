# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# could use DP table to get all left min and right max in the beginning

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            left = nums[:i+1]
            right = nums[i+1:]
            left_max = max(left)
            right_min, right_min_index = self.get_min(right)

            if left_max <= right_min:
                return i + 1

            # move index
            i = (i + 1) + right_min_index

    def get_min(self, nums):
        min_i = 0
        min_ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min_:
                min_i = i
                min_ = nums[i]
        return (min_, min_i)


print(Solution().partitionDisjoint([5,0,3,8,6]))
print(Solution().partitionDisjoint([1,1,1,0,6,12]))
print(Solution().partitionDisjoint([1,1]))
