import collections
from functools import lru_cache
from typing import List


# # 深度优先搜索
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#
#         def dfs(i, j):
#             grid[i][j] = "0"
#
#             for x, y in directs:
#                 cur_x, cur_y = x + i, y + j
#                 if 0 <= cur_x < m and 0 <= cur_y < n and grid[cur_x][cur_y] == "1":
#                     dfs(cur_x, cur_y)
#
#         res = 0
#         m, n = len(grid), len(grid[0])
#         directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     res += 1
#                     dfs(i, j)
#
#         return res

# 广度优先搜索
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i, j):
            grid[i][j] = "0"
            queue = collections.deque()
            queue.append((i, j))

            while queue:
                i, j = queue.popleft()

                for x, y in directs:
                    cur_x, cur_y = x + i, y + j
                    if 0 <= cur_x < m and 0 <= cur_y < n and grid[cur_x][cur_y] == "1":
                        grid[cur_x][cur_y] = "0"
                        queue.append((cur_x, cur_y))

        m, n = len(grid), len(grid[0])
        directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    bfs(i, j)

        return res


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]]

print(Solution().numIslands(grid))
