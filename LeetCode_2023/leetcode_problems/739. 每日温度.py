from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n, stack = len(temperatures), []
        answer = [0 for _ in range(n)]

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                answer[stack.pop()] = i - stack[-1]
            stack.append(i)

        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(Solution().dailyTemperatures(temperatures))
