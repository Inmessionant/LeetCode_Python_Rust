from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        root = [i for i in range(len(isConnected))]

        def find(x):  # 查找节点x的根结点
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)

            if rootx != rooty:
                root[rootx] = rooty

        for i in range(len(isConnected)):
            for j in range(i, len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i, j)

        return sum(i == root[i] for i in range(len(isConnected)))


isConnected = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]
print(Solution().findCircleNum(isConnected))
