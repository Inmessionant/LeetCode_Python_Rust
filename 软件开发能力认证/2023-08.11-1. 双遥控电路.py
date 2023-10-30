from typing import List


class Solution:

    def control_circuit(self, records: List[List[int]], limit: int) -> int:
        ...


records = [[0, 1], [1, 3], [2, 2], [3, 3], [4, 1], [4, 3]]
limit = 3
print(Solution().control_circuit(records, limit))
