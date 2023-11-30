from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len, cur_sum = float("inf"), 0
        left, right = 0, 0

        while right < len(nums):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

            right += 1

        return min_len if min_len != float("inf") else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(target, nums))
