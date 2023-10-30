from typing import List


class Solution:

    def control_circuit(self, records: List[List[int]], limit: int) -> int:

        status = [[] for _ in range(3)]  # status存储每个开关通电时刻序列

        for time, idx in records:
            if time not in status[idx - 1]:
                for i in range(limit):
                    status[idx - 1].append(time + i)
            else:
                while time in status[idx - 1]:
                    status[idx - 1].pop()

        return len(set(status[0]) & (set(status[1]) | set(status[2])))


records = [[0, 1],
           [1, 3],
           [2, 2],
           [3, 3],
           [4, 1],
           [4, 3]]
limit = 3
print(Solution().control_circuit(records, limit))
