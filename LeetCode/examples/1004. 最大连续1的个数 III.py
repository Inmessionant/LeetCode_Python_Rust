from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l, r, n = 0, 0, len(nums)
        reversed_zero_cnt = 0
        max_len = 0

        while r < n:
            if nums[r] == 0:
                reversed_zero_cnt += 1

            while reversed_zero_cnt > k:
                if nums[l] == 0:
                    reversed_zero_cnt -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2
print(Solution().longestOnes(nums, K))
