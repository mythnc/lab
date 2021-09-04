from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        start_row = -1
        start_col = -1
        row_len = len(mat)
        col_len = len(mat[0])
        for row in range(row_len):
            for col in range(col_len):
                if mat[row][col] == 0:
                    start_row = row
                    start_col = col
                    break
                    
            if start_row != -1:
                break

        visited = [[False] * col_len for _ in range(row_len)]
        output = [[-1] * col_len for _ in range(row_len)]
        q = [(start_row, start_col)]
        while len(q) > 0:
            # row: cell[0], col: cell[1]
            row, col = q.pop()

            if mat[row][col] == 0:
                output[row][col] = 0
            else:
                adjacents = []
                if row + 1 < row_len and visited[row+1][col]:
                    adjacents.append(output[row+1][col])
                if row - 1 >= 0 and visited[row-1][col]:
                    adjacents.append(output[row-1][col])
                if col + 1 < col_len and visited[row][col+1]:
                    adjacents.append(output[row][col+1])
                if col - 1 >= 0 and visited[row][col-1]:
                    adjacents.append(output[row][col-1])
                
                output[row][col] = min(adjacents) + 1

            visited[row][col] = True

            if row + 1 < row_len and not visited[row+1][col]:
                q.append((row+1, col))
            if row - 1 >= 0 and not visited[row-1][col]:
                q.append((row-1, col))
            if col + 1 < col_len and not visited[row][col+1]:
                q.append((row, col+1))
            if col - 1 >= 0 and not visited[row][col-1]:
                q.append((row, col-1))

        return output

print(Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(Solution().updateMatrix([[0],[0],[0],[0],[0]]))

