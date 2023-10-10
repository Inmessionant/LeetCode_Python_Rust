from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        def backtrack(start, cur_sum):

            if cur_sum == n and len(path) == k:
                res.append(path.copy())
                return

            for i in range(start, 10):
                path.append(i)
                cur_sum += i
                backtrack(i + 1, cur_sum)
                cur_sum -= i
                path.pop()

        res, path = [], []
        backtrack(1, 0)

        return res


k = 3
n = 7
print(Solution().combinationSum3(k, n))
