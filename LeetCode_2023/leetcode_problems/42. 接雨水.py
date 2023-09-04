from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        n = len(height)
        res = 0
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                bottom = height[stack.pop()]
                if not stack: break
                cur_left = height[stack[-1]]
                cur_right = height[i]
                height = min(cur_left, cur_right) - bottom
                width = i - stack[-1] - 1
                res += (width * height)

            stack.append(i)

        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
