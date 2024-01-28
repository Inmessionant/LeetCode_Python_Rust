from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        order = [[float('inf') for _ in range(n)] for _ in range(n)]
        left, top, right, bottom = 0, 0, n - 1, n - 1
        cur_number = 1

        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                order[top][col] = cur_number
                cur_number += 1
            for row in range(top + 1, bottom + 1):
                order[row][right] = cur_number
                cur_number += 1
            if left < right and top < bottom:
                for col in range(right - 1, left, - 1):
                    order[bottom][col] = cur_number
                    cur_number += 1
                for row in range(bottom, top , -1):
                    order[row][left] = cur_number
                    cur_number += 1
            left, top, right, bottom = left + 1, top + 1, right - 1, bottom - 1

        return order

n = 3
print(Solution().generateMatrix(n))