import collections
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left, right = 0, len(nums) - 1
        sorted_list = collections.deque()

        while left <= right:
            sqr_left, sqr_right = nums[left] ** 2, nums[right] ** 2
            if sqr_left >= sqr_right:
                sorted_list.appendleft(sqr_left)
                left += 1
            else:
                sorted_list.appendleft(sqr_right)
                right -= 1

        return list(sorted_list)


nums = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(nums))
