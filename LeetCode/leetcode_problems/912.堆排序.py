import heapq
import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.max_heapify(nums, 0, i)

        return nums

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def max_heapify(self, heap, root, len_heap):
        p = root
        while (2 * p + 1) < len_heap:
            l, r = 2 * p + 1, 2 * p + 2
            if r < len_heap and heap[r] > heap[l]:
                nxt = r
            else:
                nxt = l

            if heap[nxt] > heap[p]:
                heap[nxt], heap[p] = heap[p], heap[nxt]
                p = nxt
            else:
                break


heap = [5, 2, 3, 1]
print(Solution().sortArray(heap))
