class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        raw_color = image[sr][sc]
        if raw_color == newColor:
            return image

        row_len = len(image)
        col_len = len(image[0])
        queue = [(sr, sc)]
        while len(queue) > 0:
            r, c = queue.pop(0)
            image[r][c] = newColor
            for next_r, next_c in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                adj_r = r + next_r
                adj_c = c + next_c
                if (0 <= adj_r < row_len and 0 <= adj_c < col_len 
                        and image[adj_r][adj_c] == raw_color):
                    queue.append((adj_r, adj_c))

        return image

