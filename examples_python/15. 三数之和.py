from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []
        nums.sort()

        for idx, value in enumerate(nums):
            if value > 0: break
            if idx > 0 and value == nums[idx - 1]: continue

            left, right = idx + 1, n - 1

            while left < right:
                cur_three_sum = value + nums[left] + nums[right]
                if cur_three_sum == 0:
                    res.append([value, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left, right = left + 1, right - 1
                elif cur_three_sum > 0:
                    right -= 1
                else:
                    left += 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
