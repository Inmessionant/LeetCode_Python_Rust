from typing import List


class Solution:
    def merge_max(self, num1, num2):
        res = []

        while num1 or num2:
            cur = num1 if num1 > num2 else num2
            res.append(cur[0])
            cur.pop(0)
        return res

    def get_max(self, num, k):

        stack = []
        drop = len(num) - k

        for c in num:
            while drop and stack and c > stack[-1]:
                stack.pop()
                drop -= 1
            stack.append(c)
        return stack[:k]

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        res = []

        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                res.append(self.merge_max(self.get_max(nums1, i), self.get_max(nums2, k - i)))
        return max(res)


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
print(Solution().maxNumber(nums1, nums2, k))
