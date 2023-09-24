from functools import lru_cache
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        # 加一个记忆化深度搜索 `@lru_cache(None)`，核心点是从某一点出发的最长递增路径是固定的
        @lru_cache(None)
        def dfs(i, j):

            cur_res = 1

            for x, y in directs:
                cur_x, cur_y = x + i, y + j
                if 0 <= cur_x < m and 0 <= cur_y < n and matrix[cur_x][cur_y] < matrix[i][j]:
                    cur_res = max(cur_res, dfs(cur_x, cur_y) + 1)

            return cur_res

        m, n = len(matrix), len(matrix[0])
        res = 1
        directs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res


matrix = [[9, 9, 4],
          [6, 6, 8],
          [2, 1, 1]]
print(Solution().longestIncreasingPath(matrix))
