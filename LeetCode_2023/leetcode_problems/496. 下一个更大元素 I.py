from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        nums2_next_greater_element = dict()

        for idx, val in enumerate(nums2):
            while stack and val > stack[-1][1]:
                nums2_next_greater_element[stack.pop()[1]] = val
            stack.append((idx, val))

        return [nums2_next_greater_element.get(val, -1) for val in nums1]


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1, nums2))