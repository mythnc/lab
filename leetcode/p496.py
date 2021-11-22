from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_ = {}
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                hash_[stack.pop()] = num
            stack.append(num)

        return [hash_.get(num, -1) for num in nums1]


    # array
    def nextGreaterElement_array(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map = {num: i for i, num in enumerate(nums2)}

        len_nums2 = len(nums2)
        result = []
        for num in nums1:
            index = num_map[num] + 1
            is_find = False
            while index < len_nums2:
                if (first_greater_ele := nums2[index]) > num:
                    result.append(first_greater_ele)
                    is_find = True
                    break
                index += 1
            if not is_find:
                result.append(-1)

        return result


print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
print(Solution().nextGreaterElement([2,4], [1,2,3,4]))
print(Solution().nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7]))
