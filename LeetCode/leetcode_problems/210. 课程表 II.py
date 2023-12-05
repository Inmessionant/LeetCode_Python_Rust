import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 构造有向图
        graph_neighbor = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)

        for cur_course, pre_course in prerequisites:
            graph_neighbor[pre_course].append(cur_course)
            in_degree[cur_course] += 1

        queue = collections.deque()
        res = []

        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            cur_node = queue.popleft()
            res.append(cur_node)

            for neighbor_node in graph_neighbor[cur_node]:
                in_degree[neighbor_node] -= 1
                if in_degree[neighbor_node] == 0:
                    queue.append(neighbor_node)

        return res if len(res) == numCourses else []


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(Solution().findOrder(numCourses, prerequisites))
