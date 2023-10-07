import collections
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def DFS(i, j):
            ...

        def BFS():
            ...

        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()

        for i in range(rows):
            for j in range(cols):
                DFS(i, j)
                return BFS()
                

grid = [[0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]]
print(Solution().shortestBridge(grid))
