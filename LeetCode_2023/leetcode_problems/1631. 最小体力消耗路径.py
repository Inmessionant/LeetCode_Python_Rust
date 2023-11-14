import collections
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows, cols = len(heights), len(heights[0])
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        min_effort = float("-inf")

        SPT = {}
        queue = []
        queue.append((0, 0, 0))  # weight, i, j

        while queue:
            cur_max_effort, i, j = heapq.heappop(queue)
            if i == rows - 1 and j == cols - 1:
                return cur_max_effort
            if cols * i + j not in SPT:
                SPT[cols * i + j] = cur_max_effort

                for x, y in directs:
                    curx, cury = x + i, y + j
                    if 0 <= curx < rows and 0 <= cury < cols and curx * cols + cury not in SPT:
                        next_max_effort = abs(heights[curx][cury] - heights[i][j])
                        heapq.heappush(queue, (max(next_max_effort, cur_max_effort), curx, cury))
        return 0


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
print(Solution().minimumEffortPath(heights))
