class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start_i = 0
        end_i = len(nums) - 1
        
        while start_i <= end_i:
            index = (start_i + end_i) // 2
            if nums[index] == target:
                return index
            elif nums[index] > target:
                end_i = index - 1
            elif nums[index] < target:
                start_i = index + 1

        return start_i
