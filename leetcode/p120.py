from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle[-1])

        # dp index map to triangle layer (start from 0)
        dp[0] = triangle[0][0]

        # start from 2nd triangle layer
        for row in triangle[1:]:
            row_n = len(row)

            # last index
            # len in previous layer is row_n-1 (last ele is [row_n-2])
            # add 1 space for current layer
            # new space index is [row_n-1]
            dp[row_n-1] = dp[row_n-2] + row[-1]

            # from [row_n-2, 1] (inclusive)
            for i in range(row_n-2, 0, -1):
                dp[i] = min(dp[i], dp[i-1]) + row[i]

            # 1st index
            dp[0] += row[0]

            print(dp)

        return min(dp)

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(Solution().minimumTotal([[-10]]))
print(Solution().minimumTotal([[1], [2, 3]]))
print(Solution().minimumTotal([[-1],[2,3],[1,-1,-3]]))
