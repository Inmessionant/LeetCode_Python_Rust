from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:

        def backtrack(used):

            if len(path) == len(arr):
                if 0 <= path[0] * 10 + path[1] < 24 and 0 <= path[2] * 10 + path[3] <= 59:
                    res.append(list(map(str, path.copy())))
                    return True
                else: return False

            for i in range(len(arr)):
                if used[i]: continue
                path.append(arr[i])
                used[i] = True
                if backtrack(used):
                    return True
                used[i] = False
                path.pop()

        arr.sort(reverse=True)
        path, res = [], []
        used = [False for _ in range(len(arr))]
        backtrack(used)

        return "".join(res[0][:2]) + ":" + "".join(res[0][2:]) if res else ""


arr = [1, 2, 3, 4]
print(Solution().largestTimeFromDigits(arr))
