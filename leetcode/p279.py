class Solution:
    def numSquares(self, n: int) -> int:
        squar_nums = [x * x for x in range(1, 101) if x * x <= n]
        dp = [0] * (n + 1)

        for num in range(1, n+1):
            min_ = 10
            for squar_num in squar_nums:
                if squar_num > num:
                    break
                min_ = min(min_, dp[num - squar_num] + 1)
            dp[num] = min_

        return dp[n]


print(Solution().numSquares(12)) # 3
print(Solution().numSquares(13)) # 2
print(Solution().numSquares(14)) # 3
print(Solution().numSquares(15)) # 4
print(Solution().numSquares(16)) # 1
print(Solution().numSquares(100)) # 1
print(Solution().numSquares(198)) # 3
print(Solution().numSquares(9999)) # 4
