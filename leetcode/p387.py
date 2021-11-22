class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i

        #min_ = -1
        #for k in d:
        #    if d[k] > -1 and d[k]:
        #    max_ = max(max_, d[k])
        #return max_

        try:
            return min((d[k] for k in d if d[k] > -1))
        except ValueError:
            return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
