from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        max_ = 0
        for i, _ in enumerate(nums):
            if visited[i]:
                continue
            count = 0
            next_i = i
            while not visited[next_i]:
                visited[next_i] = True
                next_i = nums[next_i]
                count += 1
            max_ = max(max_, count)
            # quick way
            if max_ > (n+1)//2:
                break    
        return max_


print(Solution().arrayNesting([5,4,0,3,1,6,2]))
print(Solution().arrayNesting([0,1,2]))
