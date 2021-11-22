from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_ = 0
        row_len = len(grid)
        col_len = len(grid[0])

        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 1:
                    size = self.find_size(grid, r, c, row_len, col_len)
                    max_ = max(size, max_)

        return max_

    def find_size(self, grid, r, c, row_len, col_len):
        queue = [(r, c)]
        grid[r][c] = 0
        count = 1
        while len(queue) > 0:
            current_r, current_c = queue.pop(0)
            for next_r, next_c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                adj_r = current_r + next_r
                adj_c = current_c + next_c
                if (0 <= adj_r < row_len and 0 <= adj_c < col_len 
                        and grid[adj_r][adj_c] == 1):
                    grid[adj_r][adj_c] = 0
                    count += 1
                    queue.append((adj_r, adj_c))

        return count

print(Solution().maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))
