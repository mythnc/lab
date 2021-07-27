class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_sum = 0
        min_diff = 2**31-1
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                diff = abs(sum_ - target)
                
                # find answer
                if diff == 0:
                    return sum_

                # find min diff
                if diff < min_diff:
                    min_diff = diff
                    min_sum = sum_
                
                # adjust j and k
                if sum_ > target:
                    k -= 1
                elif sum_ < target:
                    j += 1
        return min_sum
