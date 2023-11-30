from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []
        idx = 0

        for value in pushed:

            stack.append(value)

            while stack and stack[-1] == popped[idx]:
                stack.pop()
                idx += 1

        return True if not stack and idx == len(popped) else False


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(Solution().validateStackSequences(pushed, popped))
