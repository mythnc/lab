from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # from 0 ~ n-1 and from 1 ~ n
        return max(self.dp(nums[:-1]), self.dp(nums[1:]))
    
    def dp(self, nums:List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        result = {
            0: nums[0],
            1: max(nums[0], nums[1])
        }
        for i in range(2, n):
            result[i] = max(result[i-2] + nums[i], result[i-1])

        return result[n-1]

#print(Solution().rob([2,3,2]))
#print(Solution().rob([1,2,3,1]))
#print(Solution().rob([1,2,3]))
print(Solution().rob([1,3,1,3,100]))
