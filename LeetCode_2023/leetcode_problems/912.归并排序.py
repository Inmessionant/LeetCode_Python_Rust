import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        return self.mergeSort(nums)

    def mergeSort(self, nums):

        n = len(nums)
        if n <= 1: return nums

        mid = n // 2
        left_part_sorted = self.mergeSort(nums[:mid])
        right_part_sorted = self.mergeSort(nums[mid:])

        return self.merge(left_part_sorted, right_part_sorted)

    def merge(self, left, right):

        total_soeted = []
        idx_left, idx_right = 0, 0

        while idx_left < len(left) and idx_right < len(right):
            if left[idx_left] < right[idx_right]:
                total_soeted.append(left[idx_left])
                idx_left += 1
            else:
                total_soeted.append(right[idx_right])
                idx_right += 1

        total_soeted.extend(left[idx_left:])
        total_soeted.extend(right[idx_right:])

        return total_soeted


nums = [5, 2, 3, 1]
print(Solution().sortArray(nums))
