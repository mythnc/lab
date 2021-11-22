from typing import List



class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [0] * (rowIndex + 1)
        dp[0] = 1

        for row in range(1, rowIndex+1):
            for num in range(row, 0, -1):
                dp[num] += dp[num-1]

        return dp


print(Solution().getRow(0))
print(Solution().getRow(1))
print(Solution().getRow(2))
print(Solution().getRow(3))
print(Solution().getRow(4))
print(Solution().getRow(5))
