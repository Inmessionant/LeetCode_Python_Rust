from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(start):

            if len(path) == k:
                res.append(path.copy())
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        path, res = [], []
        backtrack(1)

        return res


n = 4
k = 2
print(Solution().combine(n, k))
