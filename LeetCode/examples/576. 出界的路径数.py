from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        # 定义(i, j)为此位置，以步数为k时可以将球移出边界的路径数量
        @lru_cache(None)
        def dfs(i, j, k):

            # 注意两个判断顺序，当同时满足这两个条件时，球刚出界且maxmove=0，此时返回路径数为1
            if i < 0 or i >= m or j < 0 or j >= n: return 1
            if k == 0: return 0

            return dfs(i - 1, j, k - 1) + dfs(i + 1, j, k - 1) + dfs(i, j - 1, k - 1) + dfs(i, j + 1, k - 1)

        return dfs(startRow, startColumn, maxMove) % (10 ** 9 + 7)


m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(Solution().findPaths(m, n, maxMove, startRow, startColumn))  # res = 6
