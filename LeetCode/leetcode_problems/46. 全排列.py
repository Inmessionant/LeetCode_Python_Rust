from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(used):

            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]: continue
                path.append(nums[i])
                used[i] = True
                backtrack(used)
                used[i] = False
                path.pop()

        uesd = [False for _ in range(len(nums))]
        res, path = [], []
        backtrack(uesd)

        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
