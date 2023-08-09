from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            elif nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return False


nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
print(Solution().search(nums, target))
