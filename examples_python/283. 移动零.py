from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        len_nums, left = len(nums), -1

        for idx, right in enumerate(nums):
            if right != 0:
                left += 1
                nums[left], right = right, nums[left]

        left += 1

        for i in range(left, len_nums):
            nums[i] = 0

        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
