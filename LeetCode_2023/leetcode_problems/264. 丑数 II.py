import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        res, heap = 1, [1]
        factors = [2, 3, 5]
        seen = {1}

        for i in range(n):
            res = cur = heapq.heappop(heap)

            for factor in factors:
                if (nxt := factor * cur) not in seen:
                    heapq.heappush(heap, nxt)
                    seen.add(nxt)

        return res


n = 10
print(Solution().nthUglyNumber(n))
