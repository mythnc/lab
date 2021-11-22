from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for row in range(1, numRows):
            seq = [1]
            for i in range(row-1):
                seq.append(result[-1][i] + result[-1][i+1])
            result.append(seq + [1])

        return result


print(Solution().generate(5))
