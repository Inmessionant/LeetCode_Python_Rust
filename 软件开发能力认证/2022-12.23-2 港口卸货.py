from typing import List


class Solution:
    def getIdx(self, idx, num):  # 或者idx对应在matrix中的x, y坐标

        return idx // num, idx % num

    def get_manual_unloading_num(self, num: int, time: List[int], limit: int) -> int:
        res = 0
        matrix = [[0 for _ in range(max(time) + 1)] for _ in range(num)]
        available_start = 0  # 当前可用指示idx

        for start in time:
            expire = start + limit

            if start >= available_start:  # 可以直接装
                available_start = max(available_start, start * num)  # start对应的初始坐标
                available_start += 6
                x, y = self.getIdx(available_start, num)
                if x >= expire:  # 需要等待
                    res += 1
                    available_start -= 6
            else:
                cur_idx = available_start + 6
                x, y = self.getIdx(cur_idx, num)
                if x >= expire:
                    res += 1
                else:
                    available_start += 6

        return res


# num = 4
# time = [1, 1, 3]
# limit = 2

num = 5
time = [1, 2, 2, 3, 3, 4, 5, 5]
limit = 3
print(Solution().get_manual_unloading_num(num, time, limit))
