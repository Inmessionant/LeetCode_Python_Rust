from typing import List


class Solution:
    def __init__(self):
        self.stack = [[] for _ in range(20)]
        self.oprs = {"ADD", "MUL", "DIV"}

    def calculate(self, stack1: List[int], stack2: List[int], operate: str):

        number1 = stack1[-1] if stack1 else -1
        number2 = stack2[-1] if stack2 else -1

        if operate == "ADD":
            cur_res = number1 + number2
            if cur_res > 1024:
                cur_res %= 1024
            stack1[-1] = cur_res
            return
        elif operate == "MUL":
            cur_res = number1 * number2
            if cur_res > 1024:
                cur_res %= 1024
            stack1[-1] = cur_res
            return
        elif operate == "DIV":
            stack1[-1] = number1 // number2
            stack2[-1] = number1 % number2
            return

    def stack_calculator(self, instructions: List[str]) -> List[int]:
        instructions_lists = [instruction.strip().split() for instruction in instructions]

        for ops in instructions_lists:
            if ops[0] == "PSH":
                cur_stack = self.stack[ord(ops[1]) - ord('a')]
                if len(cur_stack) < 32:
                    cur_stack.append(int(ops[2]))
            elif ops[0] == "POP":
                cur_stack = self.stack[ord(ops[1]) - ord('a')]
                if cur_stack: cur_stack.pop()
            elif ops[0] in self.oprs:
                cur_stack1 = self.stack[ord(ops[1]) - ord('a')]
                cur_stack2 = self.stack[ord(ops[2]) - ord('a')]
                self.calculate(cur_stack1, cur_stack2, ops[0])

        res = []

        for s in self.stack:
            if not s:
                res.append(-1)
            else:
                res.append(s[-1])

        return res
