from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:


        nums.extend(nums)
        n = len(nums)
        stack = []
        res = [-1 for _ in range(n)]

        for i in range(n):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        return res[: n // 2]


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))
