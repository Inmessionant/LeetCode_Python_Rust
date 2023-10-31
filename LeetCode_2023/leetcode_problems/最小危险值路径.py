import heapq
import collections


class Solution:
    # prim
    def getMinRiskValue2(self, n, m, x, y, w):  # n个顶点，m条边， start， end， weight

        graph = collections.defaultdict(list)

        for i in range(m):
            graph[x[i]].append((y[i], w[i]))
            graph[y[i]].append((x[i], w[i]))

        mst = collections.defaultdict(list)
        max_risk = float("-inf")

        min_heap = [(weight, 0, end) for end, weight in graph[0]]

        while n not in mst:

            weight, start, end = heapq.heappop(min_heap)

            if end not in mst:
                mst[start].append((end, weight))
                mst[end].append((start, weight))
                max_risk = max(max_risk, w)

            for end_end, end_end_weight in graph[end]:
                if end_end not in mst:
                    min_heap.append((end_end_weight, end, end_end))

        return max_risk
