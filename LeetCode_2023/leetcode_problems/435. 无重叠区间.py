from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
        print(intervals)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= res[-1][1]:
                res.append(intervals[i])

        return len(intervals) - len(res)


intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
print(Solution().eraseOverlapIntervals(intervals))
