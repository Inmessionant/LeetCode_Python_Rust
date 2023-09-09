from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.K = k
        self.max_heap = []
        for num in nums:
            if len(self.max_heap) < self.K:  # 容量小于k，直接用heapq加进去
                heapq.heappush(self.max_heap, num)
            # 当len(max_heap) = k时候，因为只保留最大k个元素，所以要和miniheap[0]比较，如果比miniheap[0]大，把miniheap[0]弹出来，num加进去（heapq维护的最小堆）
            elif num > self.max_heap[0]:
                heapq.heappushpop(self.max_heap, num)

    def add(self, val: int) -> int:
        if len(self.max_heap) < self.K:
            heapq.heappush(self.max_heap, val)
        elif val > self.max_heap[0]:
            heapq.heappushpop(self.max_heap, val)

        return self.max_heap[0]


k, nums = 3, [4, 5, 8, 2]
obj = KthLargest(k, nums)
print(obj.add(3))
