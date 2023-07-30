from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        res = [-1, -1]

        if not nums:
            return res
        # nums 是一个非递减数组
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid

        if nums[l] == target:
            res[0] = l
        else:
            return res

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l + 1) // 2
            if target < nums[mid]:
                r = mid - 1
            else:
                l = mid
        res[1] = r

        return res


solution = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(solution.searchRange(nums, target))
