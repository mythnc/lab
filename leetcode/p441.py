class Solution:
    def arrangeCoins(self, n: int) -> int:
        for coin in range(1, 2 ** 31 - 1):
            n -= coin
            if n <= coin:
                return coin


print(Solution().arrangeCoins(5))
print(Solution().arrangeCoins(8))
print(Solution().arrangeCoins(10))
print(Solution().arrangeCoins(11))
