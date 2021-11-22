class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for k in d:
            if d[k] == 1:
                return k
