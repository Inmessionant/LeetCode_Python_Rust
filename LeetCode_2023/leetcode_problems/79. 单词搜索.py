from functools import lru_cache
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # k位置开始的word剩余字符，是否与(i, j)开始的board匹配(visited存储对应位置是否已经使用)
        def backtrack(i, j, k, visited):

            if board[i][j] != word[k]: return False

            if k == len(word) - 1: return True

            for x, y in directs:
                curx, cury = x + i, y + j
                if 0 <= curx < rows and 0 <= cury < cols and not visited[curx][cury]:
                    visited[curx][cury] = True
                    if backtrack(curx, cury, k + 1, visited):
                        return True
                    visited[curx][cury] = False
            return False

        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if backtrack(i, j, 0, visited):
                        return True
                    visited[i][j] = False
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(Solution().exist(board, word))
