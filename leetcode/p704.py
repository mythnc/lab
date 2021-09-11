from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums)-1

        while start_index <= end_index:
            index = (start_index + end_index) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                end_index = index - 1
            elif nums[index] < target:
                start_index = index + 1
        
        return -1


print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 2))
