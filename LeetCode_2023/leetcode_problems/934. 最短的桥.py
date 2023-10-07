import collections
import pprint
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def DFS(i, j):
            grid[i][j] = 2
            queue.append((i, j))

            for x, y in directs:
                curx, cury = x + i, y + j
                if 0 <= curx < rows and 0 <= cury < cols and grid[curx][cury] == 1:
                    DFS(curx, cury)

        def BFS():

            dist = 0

            while queue:
                size = len(queue)
                for _ in range(size):
                    i, j = queue.popleft()
                    for x, y in directs:
                        curx, cury = x + i, y + j
                        if 0 <= curx < rows and 0 <= cury < cols and grid[curx][cury] == 1:
                            return dist
                        elif 0 <= curx < rows and 0 <= cury < cols and grid[curx][cury] == 0:
                            grid[curx][cury] = 2
                            queue.append((curx, cury))
                dist += 1

        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    DFS(i, j)  # DFS之后，第一个岛屿全部变为2，且在queue里面
                    return BFS()


grid = [[0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]]
print(Solution().shortestBridge(grid))
