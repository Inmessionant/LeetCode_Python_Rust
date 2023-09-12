import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        end_times = [sorted_intervals[0][1]]

        for interval in intervals[1:]:
            if interval[0] >= end_times[0]:
                heapq.heappushpop(end_times, interval[1])
            else:
                heapq.heappush(end_times, interval[1])

        return len(end_times)


intervals = [[7, 10], [2, 4]]  # [[0, 30] ,[5, 10] ,[15, 20]]
print(Solution().minMeetingRooms(intervals))
