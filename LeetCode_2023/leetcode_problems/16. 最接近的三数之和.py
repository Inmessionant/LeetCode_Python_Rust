from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n, res = len(nums), float("inf")
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, n - 1

            while l < r:
                cur_three_sum = nums[i] + nums[l] + nums[r]
                if cur_three_sum == target: return target
                if abs(cur_three_sum - target) < abs(res - target):
                    res = cur_three_sum
                if cur_three_sum > target:
                    r -= 1
                else:
                    l += 1

        return res


nums = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(nums, target))
