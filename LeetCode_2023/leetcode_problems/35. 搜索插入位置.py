from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l


solution = Solution()
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))
