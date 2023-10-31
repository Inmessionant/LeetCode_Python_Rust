import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)

        for start, end, weight in times:
            graph[start].append((weight, end))

        SPT = {}  # shortest path tree，存的是k到每个节点最短时间
        min_heap = [(0, k)]  # 存储从节点k出发，到节点n的delay

        while min_heap:
            # 注意使用heappop弹出每次距离最短的，如果对应的node没有到达过，则对他进行更新
            delay, node = heapq.heappop(min_heap)
            if node not in SPT:
                SPT[node] = delay
                for time, next_node in graph[node]:
                    if next_node not in SPT: # 如果next_node存在spt，则在此之前一定有条路可以到达节点next_node
                        heapq.heappush(min_heap, (delay + time, next_node))

        return max(SPT.values()) if len(SPT) == n else -1


times = [[2, 1, 1],
         [2, 3, 1],
         [3, 4, 1]]
n = 4
k = 2
print(Solution().networkDelayTime(times, n, k))
