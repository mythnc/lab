from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 1:
            return [nums]

        ary = list(range(n))
        index_map = [ary]
        # get next
        next_p = self.get_next(ary[:], n)
        while next_p is not None:
            index_map.append(next_p)
            next_p = self.get_next(next_p[:], n)

        result = []
        for index_ary in index_map:
            result.append([nums[i] for i in index_ary])

        return result
        
    def get_next(self, ary, n):
        for i in range(n - 2, -1, -1):
            if ary[i] >= ary[i+1]:
                continue

            # reverse from i+1 to end
            temp = ary[i+1:]
            temp.reverse()
            ary[i+1:] = temp

            # swap
            for j in range(i+1, n):
                if ary[j] > ary[i]:
                    ary[i], ary[j] = ary[j], ary[i]
                    return ary

        return None


#print(Solution().permute([1,2,3,4]))
print(Solution().permute([0,-1,1]))
print(Solution().permute([1,2,3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))
