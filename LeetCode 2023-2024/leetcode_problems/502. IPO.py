import heapq
from pprint import pprint
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        if w >= max(capital):
            return w + sum(heapq.nlargest(k, profits))

        heap = []  # 存储当前可用利益最大的
        projects = sorted(zip(profits, capital), key=lambda x: x[1])  # 起始需要的资本从小到大

        for i in range(k):
            while projects and w >= projects[0][1]:
                heapq.heappush(heap, -projects.pop(0)[0])
            if heap:
                w -= heapq.heappop(heap)
        return w


k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print(Solution().findMaximizedCapital(k, w, profits, capital))
