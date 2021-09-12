class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            try:
                d[n].append(i)
            except KeyError:
                d[n] = [i]
        
        for k in d:
            if target - k in d:
                if k == target - k:
                    if len(d[k]) == 2:
                        return [d[k][0], d[k][1]]
                else:
                    return [d[k][0], d[target-k][0]]
