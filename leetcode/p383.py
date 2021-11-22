# question description is pretty vague
# ransomNote could use all characters in magazine
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = len(magazine)
        m = len(ransomNote)
        if n < m:
            return False

        c1 = Counter(magazine)
        c2 = Counter(ransomNote)

        print(c2-c1)

        for k in c2:
            if k not in c1:
                return False
            c1[k] -= c2[k]
            if c1[k] < 0:
                return False

        return True


print(Solution().canConstruct("a", "b"))
print(Solution().canConstruct("aa", "ab"))
print(Solution().canConstruct("aa", "aab"))
print(Solution().canConstruct("baa", "aab"))
