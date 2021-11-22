from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        head_index = 0
        tail_index = len(nums) - 1
        while head_index < tail_index:
            #print(f"{head_index=},{tail_index=}")
            mid_index = (head_index + tail_index) // 2
            #print(f"{mid_index=}")
            if nums[mid_index] == nums[mid_index+1]:
                if mid_index % 2 == 1:
                    tail_index = mid_index - 1
                else:
                    head_index = mid_index + 1
            elif nums[mid_index] == nums[mid_index-1]:
                if mid_index % 2 == 0:
                    tail_index = mid_index - 1
                else:
                    head_index = mid_index + 1
            else:
                return nums[mid_index]
        return nums[head_index]


print(Solution().singleNonDuplicate([ 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8 ]))

