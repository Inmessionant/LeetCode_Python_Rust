class Solution:
    def decodeString(self, s: str) -> str:

        res, number = "", 0
        stack = []

        for idx, val in enumerate(s):
            if val.isdigit():
                number = number * 10 + int(val)
            elif val == "[":
                stack.append([res, number])
                res, number = "", 0
            elif val == "]":
                pre_res, pre_number = stack.pop()
                res = pre_res + pre_number * res
            else:
                res += val

        return res


s = "3[a]2[bc]"
print(Solution().decodeString(s))
