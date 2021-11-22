class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        n = len(nums)
        for i in range(n):
            if (value := nums[i]) != 0:
                nums[non_zero_index] = value
                non_zero_index += 1
                
        for i in range(non_zero_index, n):
            nums[i] = 0
