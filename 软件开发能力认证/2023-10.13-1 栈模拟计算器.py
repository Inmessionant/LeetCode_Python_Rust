from typing import List

'''
题目：
使用栈模拟计算器的基本操作，该计算器共有a~t 20个栈，其中共有PUSH、POP、ADD、MUL、DIV五个操作,输出栈顶所有元素；

PUSH(stack_name， num)：将num压入对应的栈中，若栈中大小超过32，则什么都不做
POP（stack_name, num）：将栈顶对应数字弹出栈

ADD（stack_name1，stack_name2）：将栈1和栈2栈顶数字相加，并将结果更新到栈1栈顶
MUL（stack_name1，stack_name2）：将栈1和栈2栈顶数字相乘，并将结果更新到栈1栈顶
DIV（stack_name1，stack_name2）：将栈1和栈2栈顶数字相除，并将商更新到栈1栈顶，将余数更新至栈2栈顶


注意：
1.所有操作均合法（不存在POP空，除0的情况）
2.若计算结果大于1024，则对结果取余
3.若栈为空，输出-1


输入例子如下：
命令“ADD a b”，表示获得栈a、b栈顶的元素并相加，并赋值给栈a顶部元素；
命令“MUL a b”，表示获得栈a、b栈顶的元素并相减，并赋值给栈a顶部元素；
命令“PSH a 3”，表示将3入栈a；
命令“POP a ”， 表示如果栈a顶有元素就将其弹出；
命令“DIV a b”，表示获得栈a、b栈顶的元素并相除，除数赋给栈a顶，余数赋给栈b顶。
              栈顶无元素则返回-1，任意操作数值大于1024需要取模
'''


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
