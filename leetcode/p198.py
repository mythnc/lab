from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = {
            0: nums[0],
        }
        n = len(nums)
        if n >= 2:
            max_money[1] = max(max_money[0], nums[1])
        for i in range(2, n):
            max_money[i] = max(max_money[i-2] + nums[i], max_money[i-1])

        return max_money[n-1]


print(Solution().rob([1,2,3,1]))
print(Solution().rob([2,7,9,3,1]))
