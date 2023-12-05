'''
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

 -1：表示墙或是障碍物
  0：表示一扇门
INF：无限表示一个空的房间。然后，我们用 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。

你要给每个空房间位上填上该房间到最近门的距离，如果无法到达门，则填 INF 即可。
'''
import collections
from typing import List


class Solution:

    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        inf = 2147483647
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()

        # 以所有门为起点进行bfs，第一次遇到的空房间即是此房间到门的最短距离
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        dist = 1
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()
                for x, y in directs:
                    curx, cury = i + x, y + j
                    if 0 <= curx < m and 0 <= cury < n and rooms[curx][cury] == inf:
                        rooms[curx][cury] = dist
                        queue.append((curx, cury))

            dist += 1