from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        q = []
        # find all rotten oranges
        for row_index in range(row_len):
            for col_index in range(col_len):
                if grid[row_index][col_index] == 2:
                    q.append((row_index, col_index))
                    grid[row_index][col_index] = 0

        # add rotten
        count = 0
        while len(q) > 0:
            has_rotten = False
            for _ in range(len(q)):
                row_index, col_index = q.pop(0)
                for move_row, move_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    next_row = row_index + move_row
                    next_col = col_index + move_col
                    if (0 <= next_row < row_len and 0 <= next_col < col_len and 
                        grid[next_row][next_col] == 1):
                        q.append((next_row, next_col))
                        grid[next_row][next_col] = 0
                        has_rotten = True
            if has_rotten:
                count += 1

        # check never rotten cond
        for row_index in range(row_len):
            for col_index in range(col_len):
                if grid[row_index][col_index] == 1:
                    return -1

        return count


print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting([[0,2]]))
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))
