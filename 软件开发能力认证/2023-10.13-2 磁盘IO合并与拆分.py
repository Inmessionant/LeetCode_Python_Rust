from typing import List, Tuple

'''
http://oj.rnd.huawei.com/problems/3599/details

在计算机系统中，跨扇区磁盘操作较慢，需要实现一个磁盘操作的合并和拆分功能，保持磁头按照地址从小到大移动，提升系统性能。

有一个磁盘系统，磁盘地址从 0 开始；每`sectorSize` 字节作为一个扇区，如第 n （从 0 开始） 个扇区的地址区间为 [sectorSize *n, sectorSize* (n+1) - 1] 。

现给出对磁盘扇区一系列读操作 `opArray`，每个操作 `opArray[i] = [startAddr, endAddr]` （左闭右闭）。请对所有读操作的**地址区间进行合并**，然后把合并后的地址区间**按扇区进行拆分**，最后按照地址**从小到大**依次输出新的地址区间（左闭右闭）。
下图对应示例1，[0, 30], [20, 50], [10, 33] 合并后的地址区间为 [0, 50]，假如 sectorSize = 32，则拆分后的输出为 [0, 31], [32, 50] 。

**输入**

第一个参数为扇区大小 `sectorSize`，32 <= sectorSize <= 2048，且sectorSize为2的幂
第二个参数为操作列表 `opArray`，0 <= opArray.length <= 10000，0 <= opArray[i].startAddr <= opArray[i].endAddr < 2^31

**输出**

合并后的区间列表。**注意**：用例保证输出的列表大小 <= 10000


输入样例 1 
32
[[0, 30], [10, 33], [130, 150], [151, 158], [60, 100], [130, 150], [20, 50]]

输出样例 1
[[0, 31], [32, 50], [60, 63], [64, 95], [96, 100], [130, 158]]

提示样例 1
对地址区间进行合并后为 [0, 50], [60, 100], [130, 158]； 注意：[130, 150] 有两次操作。
然后按照扇区大小拆分到每个扇区上，如 [60,100] 拆分到3个扇区上，为[60, 63], [64, 95], [96, 100]；
其他依次类推。


输入样例 2
64
[[77, 128], [130, 130], [2147483502, 2147483632], [2147483600,  2147483647]]

输出样例 2
[[77, 127], [128, 128], [130, 130], [2147483502, 2147483519], [2147483520, 2147483583], [2147483584, 2147483647]]

'''

class Solution:
    def io_merge(self, sector_size: int, op_array: List[Tuple[int, int]]) -> List[Tuple[int, int]]:

        if not op_array: return []

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
