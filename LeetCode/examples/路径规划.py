# 输入
from typing import List


class Solution:
    def findAWayAcross(self, m: int, start: int, distance: List[List[int]]) -> int:

        def vaild(used):
            for i in range(m):
                if not used[i]:
                    return False
            return True

        def backtrack(start, used, cur_dist):

            global min_dist

            if vaild(used):
                min_dist = min(cur_dist, min_dist)
                return

            for i in range(m):
                if used[i]: continue
                if matrix[start][i] != float("inf"):
                    used[i] = True
                    cur_dist += matrix[start][i]
                    backtrack(i, used, cur_dist)
                    cur_dist -= matrix[start][i]
                    used[i] = False

        matrix = [[float("inf") for _ in range(m)] for _ in range(m)]
        used = [False for _ in range(m)]
        for s, e, w in distance:
            matrix[s][e] = w
            matrix[e][s] = w

        min_dist = float("inf")
        used[start] = True
        backtrack(start, used, 0)

        return min_dist if min_dist != float("inf") else -1


m, start, n = map(int, input().strip().split(' '))
distance = []
for _ in range(n):
    line = list(map(int, input().strip().split(' ')))
    distance.append(line)
