from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        result = []
        n = len(nums)
        i = 0
        while i < n - 2:
            sum_ = 0 - nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    # move j
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    # move k
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif sum_ < 0:
                    j += 1
                elif sum_ > 0:
                    k -= 1

            i += 1
            while i < n - 2 and nums[i] == nums[i-1]:
                i += 1

        return result
                
            


print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([]))
print(Solution().threeSum([0]))

