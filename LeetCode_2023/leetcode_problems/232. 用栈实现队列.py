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
# obj2 = MyQueue()
# obj2.push(x)
# param_2 = obj2.pop()
# param_3 = obj2.peek()
# param_4 = obj2.empty()
