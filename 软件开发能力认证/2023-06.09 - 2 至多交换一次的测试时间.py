import collections
from typing import List


class Solution:
    def earliest_completed_test(self, nums: List[int], board: List[List[int]]) -> int:

        len_nums, len_board = len(nums), len(board)
        number_loc = collections.defaultdict(list)  # 统计每个数字存储的坐标

        for i in range(len_board):
            for j in range(len_board):
                number_loc[board[i][j]].append((i, j))
        # 存储每行每列还需要亮灯数，初始化为len_board，即全部没有亮
        number_to_light_row, number_to_light_col = [len_board] * len_board, [len_board] * len_board

        total_light = 0
        res = 0
        for num in nums:
            res += 1
            if number_loc.get(num):
                for x, y in number_loc[num]:

                    number_to_light_row[x] -= 1
                    number_to_light_col[y] -= 1

                    total_light += 1
                    if number_to_light_row[x] == 0 or number_to_light_row[y] == 0:
                        return res
                    if number_to_light_row[x] == 1 or number_to_light_col[y] == 1 and total_light >= len_nums:
                        return res

            number_loc[num].clear()


        return -1


# nums = [6, 2, 2, 1, 7, 5, 7, 3, 4]
# board = [[4, 1, 3], [1, 2, 5], [7, 6, 2]]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [[7, 1, 2, 8], [4, 8, 6, 3], [9, 2, 1, 7], [4, 7, 6, 5]]
print(Solution().earliest_completed_test(nums, board))
