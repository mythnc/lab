from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        self.queue = []

        for r in range(self.row_len):
            for c in range(self.col_len):
                if grid[r][c] == 2:
                    self.queue.append((r, c))
                    grid[r][c] = 0

        result = self.bfs(grid)
        for r in range(self.row_len):
            for c in range(self.col_len):
                if grid[r][c] == 1:
                    return -1

        return result

    def bfs(self, grid):
        count = 0
        while len(self.queue) > 0:
            become_rooten = False
            for _ in range(len(self.queue)):
                r, c = self.queue.pop(0)

                for next_r, next_c in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                    adj_r = r + next_r
                    adj_c = c + next_c
                    if (0 <= adj_r < self.row_len and 0 <= adj_c < self.col_len
                        and grid[adj_r][adj_c] == 1):
                            grid[adj_r][adj_c] = 0
                            self.queue.append((adj_r, adj_c))
                            become_rooten = True

            if become_rooten:
                count += 1
        return count
        

print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting([[0,2]]))
