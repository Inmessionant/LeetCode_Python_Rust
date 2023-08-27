class MyQueue:

    def __init__(self):
        self.stack = []
        self.cache = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.cache:
            while self.stack:
                self.cache.append(self.stack.pop())
        return self.cache.pop()

    def peek(self) -> int:
        if self.cache:
            return self.cache[-1]
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack and not self.cache

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
