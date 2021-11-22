from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r = 0
        c = 0
        next_direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
        next_direction_index = 0
        result = [[0] * n for _ in range(n)]
        for ele in range(1, n**2+1):
            result[r][c] = ele

            next_r = r + next_direction[next_direction_index][0]
            next_c = c + next_direction[next_direction_index][1]
            if not (0 <= next_r < n and 0 <= next_c < n and result[next_r][next_c] == 0):
                next_direction_index = (next_direction_index + 1) % 4
                next_r = r + next_direction[next_direction_index][0]
                next_c = c + next_direction[next_direction_index][1]
            r, c = next_r, next_c

        return result


print(Solution().generateMatrix(1))
print(Solution().generateMatrix(2))
print(Solution().generateMatrix(3))
print(Solution().generateMatrix(10))
