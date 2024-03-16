from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(used):

            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(used)
                used[i] = False
                path.pop()

        used = [False for _ in range(len(nums))]
        nums.sort()
        path, res = [], []
        backtrack(used)

        return res


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))
