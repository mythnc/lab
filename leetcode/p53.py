from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = nums[0]
        max_ = nums[0]
        for i in range(1, n):
            if sum_ < 0:
                sum_ = nums[i]
            else:
                sum_ += nums[i]
            max_ = max(sum_, max_)
        return max_


class SolutionSlow:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -2**31
        for start_i in range(n):
            for end_i in range(start_i, n):
                max_sum = max(max_sum, sum(nums[start_i:end_i+1]))
        return max_sum 


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(Solution().maxSubArray([1])) # 1
print(Solution().maxSubArray([5,4,-1,7,8])) # 23
