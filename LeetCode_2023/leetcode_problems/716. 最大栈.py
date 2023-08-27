class MaxStack:

    def __init__(self):

        self.stack = []
        self.max_stack = [float("-inf")]

    def push(self, x):

        self.stack.append(x)
        self.max_stack.append(max(self.max_stack[-1], x))

    def pop(self):

        self.max_stack.pop()
        return self.stack.pop()

    def top(self):

        return self.stack[-1]

    def peekMax(self):

        return self.max_stack[-1]

    def popMax(self):

        max_number = self.peekMax()  # 先明确最大值

        buffer_stack = []

        while self.top() != max_number:  # 当前top值不是最大值，要先存起来
            buffer_stack.append(self.pop())  # 同时弹出stack与max_stack

        self.pop()  # 取出最大值

        while buffer_stack:
            self.push(buffer_stack.pop())

        return max_number