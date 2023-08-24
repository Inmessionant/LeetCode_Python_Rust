from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        slow, n = -1, len(nums)  # slow指向新数组上一个填充的位置

        for fast in range(n):  # fast用于寻找新数组的元素
            if nums[fast] != val:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1  # 要返回新数组长度，所以要下标+1


nums = [3, 2, 2, 3]
val = 3
print(Solution().removeElement(nums, val))
