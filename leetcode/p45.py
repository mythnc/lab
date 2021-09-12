from typing import List


class Solution:
    def jump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump_pos = 0
        min_steps = [0] * n
        for i in range(n):
            pos = nums[i] + i
            if pos > jump_pos:
                jump_pos = pos

                for j in range(1, nums[i]+1):
                    if i+j >= n:
                        break
                    if min_steps[i+j] == 0:
                        min_steps[i+j] = min_steps[i] + 1
                    else:
                        min_steps[i+j] = min(min_steps[i+j], min_steps[i] + 1)

        #print(min_steps)
        return min_steps[-1]



print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([2,3,0,1,4]))
print(Solution().canJump([0]))
print(Solution().canJump([1,1,1,1]))

