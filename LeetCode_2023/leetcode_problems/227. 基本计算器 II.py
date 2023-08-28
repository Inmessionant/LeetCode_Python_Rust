from math import floor


class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        pre_sign, cur_number = "+", 0

        for idx, char in enumerate(s):
            if char.isdigit():
                cur_number = 10 * cur_number + int(char)
            if char in "+-*/" or idx == len(s) - 1:
                if pre_sign == "+":
                    stack.append(cur_number)
                elif pre_sign == "-":
                    stack.append(-cur_number)
                elif pre_sign == "*":
                    stack.append(stack.pop() * cur_number)
                elif pre_sign == "/":
                    stack.append(int(stack.pop() / float(cur_number)))
                cur_number = 0
                pre_sign = char

        return sum(stack)


s = " 3+5 / 2 "
print(Solution().calculate(s))
