from typing import List


class Solution:
    def __init__(self):
        self.min_move = float("inf")

    def get_min_moves_num(self, planks: List[List[int]]) -> int:

        rows, cols = len(planks), len(planks[0])

        for k in range(cols):
            cur_res = [float("inf") for _ in range(rows)]
            for i in range(rows):
                for j in range(cols):
                    if planks[i][j] == 1:
                        cur_res[i] = min(cur_res[i], abs(j - k))
            self.min_move = min(self.min_move, sum(cur_res))

        return self.min_move


planks = [[1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 0, 0, 0, 0]]
planks = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]]
print(Solution().get_min_moves_num(planks))
