from typing import List


class Solution:
    def earliest_completed_test(self, nums: List[int], board: List[List[int]]) -> int:
        ...


nums = [6, 2, 2, 1, 7, 5, 7, 3, 4]
board = [[4, 1, 3], [1, 2, 5], [7, 6, 2]]
print(Solution().earliest_completed_test(nums, board))
