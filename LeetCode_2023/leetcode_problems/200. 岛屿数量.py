from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ...


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]]

print(Solution().numIslands(grid))
