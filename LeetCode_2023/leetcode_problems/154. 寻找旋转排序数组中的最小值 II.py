from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:  # 可能存在重复元素值的数组 nums

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:  # 当中间元素大于右侧元素时意味着最小元素在右侧
                l = mid + 1
            elif nums[mid] == nums[r]:  # nums[r]=nums[mid]，没办法判断，r往前移，然后判断
                r -= 1
            else:
                r = mid  # 当中间元素小于右侧元素时意味着拐点即最小元素在左侧，左边界mid会分在左边

        return nums[l]


nums = [2, 2, 2, 0, 2]
print(Solution().findMin(nums))
