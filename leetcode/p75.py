from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counting_len = 3
        counting = [0] * counting_len
        for num in nums:
            counting[num] += 1

        for i in range(1, counting_len):
            counting[i] += counting[i-1]

        n = len(nums)
        result = [None] * n
        for i in range(n-1, -1, -1):
            num = nums[i]
            result[counting[num]-1] = num
            counting[num] -= 1

        nums[:] = result





print(Solution().sortColors([2,0,2,1,1,0]))
print(Solution().sortColors([2,0,1]))
print(Solution().sortColors([0]))
print(Solution().sortColors([1]))
        
