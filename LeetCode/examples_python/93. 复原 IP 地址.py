from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def validNumber(start, end):
            if not s[start: end + 1]:
                return False
            elif s[start] == "0" and start != end:
                return False
            elif int(s[start: end + 1]) < 0 or 255 < int(s[start: end + 1]):
                return False
            return True

        def backtrack(start):

            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return

            for i in range(start, len(s)):
                if validNumber(start, i):
                    path.append(s[start: i + 1])
                    backtrack(i + 1)
                    path.pop()
                else:
                    break

        path, res = [], []
        if len(s) < 4 or len(s) > 12: return []

        backtrack(0)

        return res

s = "25525511135"
print(Solution().restoreIpAddresses(s))