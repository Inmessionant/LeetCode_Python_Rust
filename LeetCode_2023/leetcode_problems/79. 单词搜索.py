from functools import lru_cache
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        @lru_cache(None)
        def DFS(i, j, k):
            if board[i][j] != word[k]:
                return False
            if len(word) - 1 == k:
                return True

            for x, y in directs:
                curx, cury = x + i, y + j
                if 0 <= curx < rows and 0 <= cury < cols:
                    if DFS(curx, cury, k + 1):
                        print(curx, cury, k + 1)
                        return True
            return False

        rows, cols = len(board), len(board[0])
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if DFS(i, j, 0):
                        return True
        return False


board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCB"
print(Solution().exist(board, word))
