import heapq
from pprint import pprint
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        stack = [(matrix[0][0], 0, 0)]
        res = matrix[0][0]
        seen = set()

        while k:
            res, i, j = heapq.heappop(stack)
            # print(k, ": ", res, i, j)
            for cur_i, cur_j in [(0, 1), (1, 0)]:
                if i + cur_i < len(matrix) and j + cur_j < len(matrix[0]) and (i + cur_i, j + cur_j) not in seen:
                    heapq.heappush(stack, (matrix[i + cur_i][j + cur_j], i + cur_i, j + cur_j))
                    seen.add((i + cur_i, j + cur_j))
            # pprint(stack)
            k -= 1

        return res


matrix = [[1, 3, 5],
          [6, 7, 12],
          [11, 14, 14]]
k = 6
print(Solution().kthSmallest(matrix, k))
