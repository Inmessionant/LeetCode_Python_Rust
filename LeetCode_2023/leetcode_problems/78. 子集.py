from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start):

            res.append(path.copy())

            if start >= len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        path, res = [], []
        backtrack(0)

        return res


nums = [1, 2, 3]
print(Solution().subsets(nums))