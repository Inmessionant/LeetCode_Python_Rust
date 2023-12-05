

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if stack:
                    if c == ")" and stack.pop() != "(":
                        return False
                    elif c == "]" and stack.pop() != "[":
                        return False
                    elif c == "}" and stack.pop() != "{":
                        return False

                else:
                    return False

        return True if not stack else False

s = "()[]{}"
print(Solution().isValid(s))