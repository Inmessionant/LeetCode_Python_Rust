from typing import List


class Solution:
    def get_manual_unloading_num(self, num: int, time: List[int], limit: int) -> int:
        ...


num = 5
time = [1 ,2 ,2 ,3 ,3 ,4 ,5 ,5]
limit = 3
print(Solution().get_manual_unloading_num(num, time))
