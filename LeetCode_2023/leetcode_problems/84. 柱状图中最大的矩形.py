from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        heights = [0] + heights + [0]
        res = 0
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                if not stack: break
                cur_width = i - stack[-1] -1
                res = max(res, cur_width * cur_height)

            stack.append(i)

        return res


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
