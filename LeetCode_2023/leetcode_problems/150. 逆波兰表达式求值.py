from typing import List


class Solution:
    def cal(self, comp1, comp2, opr):
        if opr == "+":
            return comp1 + comp2
        elif opr == "-":
            return comp1 - comp2
        elif opr == "*":
            return comp1 * comp2
        elif opr == "/":
            return int(comp1 / float(comp2))

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for char in tokens:
            if char in "+-*/":
                comp2 = stack.pop()
                comp1 = stack.pop()
                stack.append(self.cal(comp1, comp2, char))
            else:
                stack.append(int(char))

        return stack[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))
