from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums, pre_non_zero = len(nums), -1

        for idx, cur_value in enumerate(nums):
            if cur_value != 0:
                pre_non_zero += 1
                nums[pre_non_zero], cur_value = cur_value, nums[pre_non_zero]

        pre_non_zero += 1

        for i in range(pre_non_zero, len_nums):
            nums[i] = 0

        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
