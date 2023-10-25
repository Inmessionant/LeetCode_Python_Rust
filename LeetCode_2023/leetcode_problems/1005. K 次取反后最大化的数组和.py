import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        for i in range(k):
            heapq.heappush(nums, -heapq.heappop(nums))

        return sum(nums)


nums = [3, -1, 0, 2]
k = 3
print(Solution().largestSumAfterKNegations(nums, k))
