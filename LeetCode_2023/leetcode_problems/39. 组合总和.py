from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start, sumpath):

            if sumpath > target:  # 剪枝, 由于backtrack一直调用i位置，会无限循环下去
                return

            if sumpath == target:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                sumpath += candidates[i]
                backtrack(i, sumpath)  # 关键点:不用i + 1了，表示candidates中的数字可以重复读取当前的数
                sumpath -= candidates[i]
                path.pop()

        res, path = [], []
        backtrack(0, 0)

        return res


candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
