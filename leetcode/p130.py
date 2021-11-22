from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row_n = len(board)
        self.col_n = len(board[0])

        # check border
        # check first line and last line
        q = []
        rows = [0] if self.row_n <= 1 else [0, self.row_n-1]
        for r_index in rows:
            for c_index in range(self.col_n):
                if board[r_index][c_index] == 'O':
                    q.append((r_index, c_index))

        # check first col and last col
        cols = [0] if self.col_n <= 1 else [0, self.col_n-1]
        for c_index in cols:
            for r_index in range(self.row_n):
                if board[r_index][c_index] == 'O':
                        q.append((r_index, c_index))

        # change border 'O' to 'A'
        while len(q) > 0:
            for _ in range(len(q)):
                r, c = q.pop(0)
                board[r][c] = 'A'
                for r_point, c_point in ((1, 0), (-1, 0), (0, -1), (0, 1)):
                    next_r = r + r_point
                    next_c = c + c_point

                    if (0 <= next_r < self.row_n and 0 <= next_c < self.col_n
                            and board[next_r][next_c] == 'O'):
                        q.append((next_r, next_c))

        # change other 'O' to 'X'
        self.change(board, 'O', 'X')
        # change 'A' to 'O'
        self.change(board, 'A', 'O')
        # or could be hard-coding

    # naming: flip!?
    def change(self, board, old_char, new_char):
        for row_i in range(self.row_n):
            for col_i in range(self.col_n):
                if board[row_i][col_i] == old_char:
                    board[row_i][col_i] = new_char


print(Solution().solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]))
