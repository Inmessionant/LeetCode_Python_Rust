from typing import List, Tuple


class Solution:
    def io_merge(self, sector_size: int, op_array: List[Tuple[int, int]]) -> List[Tuple[int, int]]:

        if not op_array:  return []

        op_array.sort(key=lambda x: x[0])

        merged_array = [op_array[0]]

        for i in range(1, len(op_array)):
            if op_array[i][0] <= merged_array[-1][1] + 1:
                merged_array[-1][1] = max(merged_array[-1][1], op_array[i][1])
            else:
                merged_array.append(op_array[i])

        res = []

        for cur_array in merged_array:
            start, end = cur_array[0], cur_array[1]
            start_block, end_block = start // sector_size, end // sector_size

            for i in range(start_block, end_block + 1):
                cur_start = max(start, i * sector_size)
                cur_end = min(sector_size * (i + 1) - 1, end)
                res.append((cur_start, cur_end))

        return res


sector_size = 64
op_array = [[77, 128], [130, 130], [2147483502, 2147483632], [2147483600,  2147483647]]
print(Solution().io_merge(sector_size, op_array))
