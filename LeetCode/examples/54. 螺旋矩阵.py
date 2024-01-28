from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows, cols = len(matrix), len(matrix[0])
        left, top, right, bottom = 0, 0, cols - 1, rows - 1
        res = []

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom, top , -1):
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return res


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(Solution().spiralOrder(matrix))
