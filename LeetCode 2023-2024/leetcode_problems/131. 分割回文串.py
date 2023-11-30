from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(start):

            if start == len(s):
                res.append(path.copy())
                return

            for i in range(start, len(s)):
                if s[start: i + 1] == s[start: i + 1][::-1]:
                    path.append(s[start: i + 1])
                else:
                    continue
                backtrack(i + 1)
                path.pop()

        path, res = [], []
        backtrack(0)

        return res


s = "aab"
print(Solution().partition(s))
