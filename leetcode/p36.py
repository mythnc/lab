from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid(row):
                #print('row gg')
                return False

        for col in zip(*board):
            if not self.is_valid(col):
                #print('col gg')
                return False

        # 3 * 3
        row = 0
        col = 0
        movement = (0, 1, 2)
        for r_start_index in range(0, 9, 3):
            for c_start_index in range(0, 9, 3):
                visited = [False] * 9
                r_index = r_start_index
                c_index = c_start_index
                for r_move in movement:
                    for c_move in movement:
                        r_index = r_start_index + r_move
                        c_index = c_start_index + c_move
                        d = board[r_index][c_index]
                        if d == '.':
                            continue
                        if visited[int(d)-1]:
                            #print('3x3 gg')
                            return False
                        visited[int(d)-1] = True
        return True

    def is_valid(self, ary):
        visited = [False] * 9
        for d in ary:
            if d == '.':
                continue
            if visited[int(d)-1]:
                return False
            visited[int(d)-1] = True
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))
