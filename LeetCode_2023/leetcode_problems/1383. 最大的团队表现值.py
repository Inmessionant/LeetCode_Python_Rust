from pprint import pprint
from typing import List
import heapq


# class Solution:  # 1.去掉最多k个工程师限制
#     def maxPerformance(self, n: int, speed: List[int], efficiency: List[int]) -> int:
#         max_performance, sum_speed = 0, 0
#         sorted_people = sorted(zip(speed, efficiency), key=lambda x: -x[1])
#
#         for i, (s, e) in enumerate(sorted_people):
#             sum_speed += s
#             max_performance = max(max_performance, sum_speed * e)
#
#         return max_performance % (10 ^ 9 + 7)
#
#
# n = 6
# speed = [2, 10, 3, 1, 5, 8]
# efficiency = [5, 4, 3, 9, 7, 2]
# print(Solution().maxPerformance(n, speed, efficiency))


class Solution:  # 2.
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        max_performance, sum_speed = 0, 0
        heap = []
        sorted_people = sorted(zip(speed, efficiency), key=lambda x: -x[1])

        for i, (s, e) in enumerate(sorted_people):
            if i < k:
                heapq.heappush(heap, s)
                sum_speed += s
            elif s > heap[0]:
                sum_speed += s - heapq.heappushpop(heap, s)
            max_performance = max(max_performance, sum_speed * e)

        return max_performance % (1000000007)


n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2
print(Solution().maxPerformance(n, speed, efficiency, k))
