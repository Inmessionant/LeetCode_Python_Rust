from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) - 1

        while l < r:
            mid = l + (r - l) // 2
            if matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid

        if matrix[l][0] == target:
            return True

        row = l if target > matrix[l][0] else l - 1
        l, r = 0, len(matrix[0]) - 1

        while l < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid

        if matrix[row][l] == target:
            return True
        else:
            return False


matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3

solution = Solution()
print(solution.searchMatrix(matrix, target))
