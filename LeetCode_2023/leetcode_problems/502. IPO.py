from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ...

k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
print(Solution().findMaximizedCapital(k, w, profits, capital))