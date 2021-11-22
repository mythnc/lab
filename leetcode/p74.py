from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        # find row
        for row in matrix:
            if row[0] <= target <= row[-1]:
                # bin search
                i = 0
                j = n - 1
                while i <= j:
                    middle = (i + j) // 2
                    if row[middle] == target:
                        return True
                    elif target < row[middle]:
                        j = middle - 1
                    elif target > row[middle]:
                        i = middle + 1

        return False
        

print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # F
print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # T
print(Solution().searchMatrix([[1,3]], 3)) # T

