from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        output = []
        matrix.reverse()
        for ele in zip(*matrix):
            output.append(list(ele))

        matrix[:] = output
        print(matrix)



print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
