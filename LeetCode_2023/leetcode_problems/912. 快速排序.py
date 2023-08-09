import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        self.quickSort(nums, 0, len(nums) - 1)

        return nums

    def quickSort(self, nums, left, right):

        if left >= right: return

        position = self.partation(nums, left, right)
        self.quickSort(nums, left, position - 1)
        self.quickSort(nums, position + 1, right)

    def partation(self, nums, left, right):

        pivot = random.randint(left, right)

        nums[pivot], nums[right] = nums[right], nums[pivot]
        pre_min_pivot = left - 1

        for cur_pos in range(left, right):
            if nums[cur_pos] < nums[right]:
                pre_min_pivot += 1
                nums[pre_min_pivot], nums[cur_pos] = nums[cur_pos], nums[pre_min_pivot]

        pre_min_pivot += 1
        nums[pre_min_pivot], nums[right] = nums[right], nums[pre_min_pivot]

        return pre_min_pivot


nums = [5, 2, 3, 1]
print(Solution().sortArray(nums))
