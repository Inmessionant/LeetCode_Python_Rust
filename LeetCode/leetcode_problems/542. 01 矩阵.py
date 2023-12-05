import collections
from typing import List

'''
**超级源点是0：从超级源点0(多个0源点)到其他点的最短路, 反过来就是其他点到超级源点0的最短距离, 也就是题目要求的东西；**

你理解这个做法后, **如果超级源点是1, 就是从1这个点去更新其他点, 那么你求得就是从超级源点1到其他点的最短路, 反过来就是从其他点走到1的最短距离,** 而题目求得是其他点到0的最短距离；

多说一句, **添加超级源点后, 多源就转化为单源了, 这是一个常见的技巧.**

还有一个**常见的技巧是建反向边**, 类似于本题, 本来是求1到0的最短距离, 因为从1到0的最短路和从0到1的最短路肯定是同一条路径, 所以反过来求0到1的最短路.

**思路 :** 从 0 开始 BFS, 遇到距离最小值需要更新的则更新后重新入队更新后续结点
'''


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        res = [[None for _ in range(n)] for _ in range(m)]
        queue = collections.deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    res[i][j] = 0

        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = 1
        while queue:
            size = len(queue)

            for _ in range(size):
                i, j = queue.popleft()
                for x, y in directs:
                    curx, cury = x + i, y + j
                    if 0 <= curx < m and 0 <= cury < n and res[curx][cury] == None:
                        res[curx][cury] = dist
                        queue.append((curx, cury))

            dist += 1

        return res


mat = [[0, 0, 0],
       [0, 1, 0],
       [0, 0, 0]]
print(Solution().updateMatrix(mat))
