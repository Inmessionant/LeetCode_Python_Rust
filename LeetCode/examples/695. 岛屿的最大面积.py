import collections
from typing import List


# 广度优先搜索
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(i, j):
            grid[i][j] = 0
            area = 0
            queue = collections.deque()
            queue.append((i, j))

            while queue:
                i, j = queue.popleft()
                area += 1

                for x, y in directs:
                    curx, cury = x + i, y + j
                    if 0 <= curx < m and 0 <= cury < n and grid[curx][cury] == 1:
                        # 需要注意的是，添加时候就要置0，否则会重复添加，例如处理(0, 1)(-1, 0)时不在添加时候置为0而是在pop时候置为0，则会重复添加(1, 1)元素
                        grid[curx][cury] = 0
                        queue.append((curx, cury))

            return area

        m, n = len(grid), len(grid[0])
        res = 0
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))

        return res


grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]

print(Solution().maxAreaOfIsland(grid))
