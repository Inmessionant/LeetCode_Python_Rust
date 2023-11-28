from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sum_nums = sum(nums)
        if sum_nums % 2 == 1: return False
        target = sum_nums // 2

        dp = [0 for _ in range(target + 1)]

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return dp[-1] == target


nums = [1, 5, 11, 5]
print(Solution().canPartition(nums))
