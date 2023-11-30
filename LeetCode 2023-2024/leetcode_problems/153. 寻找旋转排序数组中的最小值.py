from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 确认需要找最小的那个数，从左到右找到第一个最小的数
        # 当中间元素大于右侧元素时意味着拐点即最小元素在右侧，否则在左侧
        # nums 中的所有整数互不相同
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]


nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))
