from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_result = 0
        for num in nums:
            xor_result ^= num

        # find partition index
        partition_index = 1
        while (partition_index & xor_result) == 0:
            partition_index <<= 1

        num1 = 0
        num2 = 0
        for num in nums:
            if (num & partition_index) == 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]


print(Solution().singleNumber([1,2,1,3,2,5]))
print(Solution().singleNumber([-1,0]))
print(Solution().singleNumber([0,1]))
print(Solution().singleNumber([0,1,1,2]))
print(Solution().singleNumber([1,1,0, -2147483648]))
