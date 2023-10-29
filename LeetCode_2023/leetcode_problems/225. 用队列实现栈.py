import collections


class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)

        for _ in range(n):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj2 = MyStack()
# obj2.push(x)
# param_2 = obj2.pop()
# param_3 = obj2.top()
# param_4 = obj2.empty()
