from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        root = [i for i in range(len(edges) + 1)]

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                root[root_x] = root_y

        for x, y in edges:
            if find(x) != find(y):
                union(x, y)
            else:
                return [x, y]


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(Solution().findRedundantConnection(edges))
