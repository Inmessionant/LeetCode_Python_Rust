from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def backtrack(start):

            if start == len(digits):
                res.append("".join(path.copy()))
                return

            for val in num2char[digits[start]]:
                path.append(val)
                backtrack(start + 1)
                path.pop()

        num2char = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['h', 'i', 'g'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not digits: return []

        path, res = [], []
        backtrack(0)

        return res


digits = "23"
print(Solution().letterCombinations(digits))
