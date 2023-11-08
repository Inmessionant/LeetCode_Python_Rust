from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        min_step, cur_cover, next_cover = 0, 0, 0

        for i in range(len(nums)):
            if i > cur_cover:
                min_step += 1
                cur_cover = next_cover
            next_cover = max(next_cover, i + nums[i])

        return min_step


nums = [2, 3, 1, 1, 4]
print(Solution().jump(nums))
