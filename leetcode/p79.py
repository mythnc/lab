from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_index, row in enumerate(board):
            for col_index, letter in enumerate(row):
                if letter != word[0]:
                    continue
                # do DFS
                if self.find_word(row_index, col_index, board, word):
                    return True
        return False
                
    def find_word(self, row_index, col_index, board, word) -> bool:
        row_n = len(board)
        col_n = len(board[0])
        visited = [[False] * col_n for _ in range(row_n)]
        
        visited[row_index][col_index] = True
        return self.dfs(row_index, col_index, board, word, 1, visited)

    def dfs(self, row_index, col_index, board, word, word_index, visited):
        if word_index >= len(word):
            return True

        row_n = len(board)
        col_n = len(board[0])
        row_movement = [0, 1, 0, -1]
        col_movement = [1, 0, -1, 0]
        for i in range(4):
            next_row_index = row_index + row_movement[i]
            next_col_index = col_index + col_movement[i]
            
            if (next_row_index < 0 or next_col_index < 0 
                or next_row_index >= row_n or next_col_index >= col_n
                or visited[next_row_index][next_col_index]
                or board[next_row_index][next_col_index] != word[word_index]):
                    continue

            visited[next_row_index][next_col_index] = True
            if self.dfs(next_row_index, next_col_index, board, word, word_index+1, visited):
                return True
            visited[next_row_index][next_col_index] = False

        return False


print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(Solution().exist([["a", "b"],["c", "d"]], "abcd"))
print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))
print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
