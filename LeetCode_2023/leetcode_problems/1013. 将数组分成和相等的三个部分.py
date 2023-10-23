from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        def backtrack(start):
            if len(path) == 3 and start == len(arr):
                res.append(path.copy())
                return

            for i in range(start, len(arr)):
                if sum(arr[start: i + 1]) == part_total:
                    path.append(arr[start: i + 1])
                else:
                    continue
                backtrack(i + 1)
                path.pop()

        total = sum(arr)
        if (total % 3) != 0: return False
        part_total = total / 3

        path, res = [], []
        backtrack(0)

        return True if res else False


arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
print(Solution().canThreePartsEqualSum(arr))
