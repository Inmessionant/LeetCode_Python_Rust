from functools import lru_cache
from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        def resume_matrix(locations):

            matrix = [[0 for _ in range(n)] for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    if i != j:
                        matrix[i][j] = matrix[j][i] = abs(locations[i] - locations[j])
            return matrix

        @lru_cache(None)
        # 在位置 pos 出发，油量为 rest 的前提下，到达 end 的「路径数量」
        def dfs(pos, rest):

            if cost[pos][finish] > rest:
                return 0
            ans = 1 if pos == finish else 0

            for next_pos in range(n):
                if next_pos != pos:
                    ans += dfs(next_pos, rest - cost[pos][next_pos])

            return ans

        n = len(locations)
        cost = resume_matrix(locations)

        return dfs(start, fuel) % (10 ** 9 + 7)


locations = [2, 3, 6, 8, 4]
start = 1
finish = 3
fuel = 5
print(Solution().countRoutes(locations, start, finish, fuel))
