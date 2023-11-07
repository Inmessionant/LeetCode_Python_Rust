from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:  # 模拟

        n = len(nums)
        if n < 2: return n

        prediff = nums[1] - nums[0]
        res = 2 if prediff != 0 else 1  # 第1个diff不等于0时，就有2个元素在摆动序列，如[1, 17]

        for i in range(2, n):
            curdiff = nums[i] - nums[i - 1]
            # nums = [3,3,3,2,5]，当前面一直是连续，之后有改变时候，序列数也会增加，则需要考虑prediff == 0
            if (curdiff > 0 and prediff <= 0) or (curdiff < 0 and prediff >= 0):
                res += 1
                prediff = curdiff

        return res


nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(Solution().wiggleMaxLength(nums))
