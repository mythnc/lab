from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )
        row = len(matrix)
        col = len(matrix[0])
        total = row * col
        count = 0
        d_index = 0
        result = [0] * total
        r = 0
        c = 0
        VISITED_VALUE = 101
        while count < total:
            result[count] = matrix[r][c]
            matrix[r][c] = VISITED_VALUE
            count += 1
            if count >= total:
                break
            next_r, next_c = directions[d_index]
            while (not ((0 <= r+next_r < row) and (0 <= c+next_c < col)
                and matrix[r+next_r][c+next_c] != VISITED_VALUE)):
                d_index = (d_index + 1) % len(directions)
                next_r, next_c = directions[d_index]
            r += next_r
            c += next_c

        return result


print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
