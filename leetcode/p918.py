from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = nums[0]
        min_ = nums[0]
        sum_max = nums[0]
        sum_min = nums[0]
        sum_ = nums[0]
        for i in range(1, n):
            if sum_max < 0:
                sum_max = nums[i]
            else:
                sum_max += nums[i]
            max_ = max(sum_max, max_)

            if sum_min > 0:
                sum_min = nums[i]
            else:
                sum_min += nums[i]
            min_ = min(sum_min, min_)

            sum_ += nums[i]

        return max(max_, sum_ - min_) if max_ > 0 else max_


class SolutionSlow:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -2**31
        for start_index in range(n):
            sub_max_sum = nums[start_index]
            sum_ = sub_max_sum

            # each circular array
            #print(start_index, start_index+n)
            #for i in range(start_index, start_index + n):
            #    print(nums[i % n], end=" ")
            #print()

            for i in range(start_index+1, start_index + n):
                value = nums[i % n]
                if sum_ < 0:
                    sum_ = value
                else:
                    sum_ += value
                sub_max_sum = max(sum_, sub_max_sum)
            #print(sub_max_sum)

            max_sum = max(max_sum, sub_max_sum)
        return max_sum

print(Solution().maxSubarraySumCircular([1,-2,3,-2]))
#print()
print(Solution().maxSubarraySumCircular([5,-3,5]))
#print()
print(Solution().maxSubarraySumCircular([3,-1,2,-1]))
#print()
print(Solution().maxSubarraySumCircular([3,-2,2,-3]))
#print()
print(Solution().maxSubarraySumCircular([-2,-3,-1]))
#print()

