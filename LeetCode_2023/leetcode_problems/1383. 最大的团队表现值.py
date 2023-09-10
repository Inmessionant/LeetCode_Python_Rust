from typing import List


class Solution:  # 1.去掉最多k个工程师限制
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int]) -> int:
        ...


n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
print(Solution().maxPerformance(n, speed, efficiency))


# class Solution: # 2.
#     def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
#         ...
#
#
# n = 6
# speed = [2, 10, 3, 1, 5, 8]
# efficiency = [5, 4, 3, 9, 7, 2]
# k = 2
# print(Solution().maxPerformance(n, speed, efficiency, k))
