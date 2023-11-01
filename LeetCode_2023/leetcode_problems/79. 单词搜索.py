from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ...


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "SEE"
print(Solution().exist(board, word))
