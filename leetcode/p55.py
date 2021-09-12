from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump_pos = 0
        for i in range(n):
            if i > jump_pos:
                break
            jump_pos = max(jump_pos, nums[i] + i)
        return jump_pos >= n-1



print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
print(Solution().canJump([0]))

