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

    def popMax(self):  # 这个函数比较特殊

        max_number = self.peekMax()

        buffer_stack = []

        while self.top() != max_number:
            buffer_stack.append(self.pop())

        self.pop()

        while buffer_stack:
            self.push(buffer_stack.pop())

        return max_number