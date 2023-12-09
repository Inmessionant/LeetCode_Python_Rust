import collections
from typing import List, Tuple, Counter


class Node:
    def __init__(self, val):
        self.value = val
        self.childs = []


class Solution:
    def __init__(self):
        self.map = {}

    def buildTree(self, areas):

        all_area = set()  # 所有area，包括root
        all_cur_area = set()  # 不包括root

        for cur_area, parent_area in areas:
            if cur_area not in self.map:
                self.map[cur_area] = Node(cur_area)
            if parent_area not in self.map:
                self.map[parent_area] = Node(parent_area)
            self.map[parent_area].childs.append(self.map[cur_area])

            all_area.add(cur_area)
            all_area.add(parent_area)
            all_cur_area.add(cur_area)

        root_str = all_area.difference(all_cur_area)

        return list(root_str)[0]

    def vaildStr(self, counter_keyword, cur_str):
        counter_cur_str = Counter(cur_str)

        for key, value in counter_keyword.items():
            if key not in counter_cur_str:
                return False
            if value > counter_cur_str[key]:
                return False

        return True

    def matchNode(self, root: str, keyword: str) -> set:

        match_node = set()
        counter_keyword = Counter(keyword)

        queue = collections.deque()
        queue.append(self.map[root])

        while queue:
            node = queue.popleft()
            if self.vaildStr(counter_keyword, node.value):
                match_node.add(node.value)

            for child in node.childs:
                queue.append(child)

        return match_node

    def match_paths(self, areas: List[Tuple[str, str]], keyword: str) -> int:
        # 1.构建树结构，要知道根节点
        root_str = self.buildTree(areas)

        # 2.从根节点开始匹配，找到匹配的所有节点
        match_node = self.matchNode(root_str, keyword)

        # 3.从根节点开始回溯，找到所有路径，如果路径中包含匹配到的节点，res += 1
        def isVaildPath(match_node, path):
            for node in match_node:
                if node in path:
                    return True
            return False

        def backtrack(node):

            if not node.childs and isVaildPath(match_node, path):  # todo：增加判断路径在path中
                res.append(path.copy())
                return

            for child in node.childs:
                path.append(child.value)
                backtrack(child)
                path.pop()

        res, path = [], [root_str]
        backtrack(self.map[root_str])

        return len(res)
