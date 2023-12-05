from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start):

            if len(path) >= 2:
                res.append(path.copy())

            if start >= len(nums): return

            seen = set()

            for i in range(start, len(nums)):

                if nums[i] in seen: continue
                if path and nums[i] < path[-1]: continue

                seen.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        res, path = [], []
        backtrack(0)

        return res


nums = [4, 6, 7, 7]
print(Solution().findSubsequences(nums))
