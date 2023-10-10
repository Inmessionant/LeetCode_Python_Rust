from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, sumpath):

            if sumpath > target:
                return

            if sumpath == target:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                sumpath += candidates[i]
                backtrack(i + 1, sumpath)
                sumpath -= candidates[i]
                path.pop()

        path, res = [], []
        candidates.sort()
        backtrack(0, 0)

        return res


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(Solution().combinationSum2(candidates, target))
