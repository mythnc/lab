from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [n for n in range(1, n+1)]

        return self.recursive(numbers, k)

    def recursive(self, ary, k):
        #print(ary)
        n = len(ary)
        if k > n:
            return []

        result = []
        for i in range(n):
            prefix = ary[i]
            if k == 1:
                result.append([prefix])
                continue

            others = self.recursive(ary[i+1:], k-1)
            if len(others) == 0:
                continue
            result.extend([[prefix] + ele for ele in others])
        #print(result)
        return result



print(Solution().combine(4, 2))
print(Solution().combine(1,1))
print(Solution().combine(4, 3))
print(Solution().combine(5, 3))
print(Solution().combine(5, 1))
