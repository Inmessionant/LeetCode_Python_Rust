from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ...


mat = [[0, 0, 0],
       [0, 1, 0], 
       [0, 0, 0]]
print(Solution().updateMatrix(mat))
