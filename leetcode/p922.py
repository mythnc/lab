from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        j = 1
        while i < n and j < n:
            while i < n and self.is_even(i, nums):
                i += 2
            while j < n and self.is_odd(j, nums):
                j += 2

            if i >= n or j >= n:
                break

            nums[i], nums[j] = nums[j], nums[i]
             
        return nums

    def is_even(self, i, nums):
        return i % 2 == 0 and nums[i] % 2 == 0

    def is_odd(self, i, nums):
        return i % 2 == 1 and nums[i] % 2 == 1

print(Solution().sortArrayByParityII([4,2,5,7]))
print(Solution().sortArrayByParityII([2,3]))

