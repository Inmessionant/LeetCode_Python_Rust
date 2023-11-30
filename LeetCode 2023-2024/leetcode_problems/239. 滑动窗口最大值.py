from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l, r, n = 0, k, len(nums)  # l其实没使用
        max_heap = [(-nums[i], i) for i in range(k)]  # python默认最小堆
        heapify(max_heap)
        res = [-max_heap[0][0]]

        while r < n:
            heappush(max_heap, (-nums[r], r))

            while max_heap[0][1] <= r - k:  # 不满足条件,最大值在窗口外
                heappop(max_heap)

            res.append(-max_heap[0][0])  # 更新结果
            r += 1

        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
