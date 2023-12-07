import collections
from typing import Tuple, List


class Node:
    def __init__(self, node):
        self.node_str = node
        self.childs = []


class Solution:
    def __init__(self):
        self.node_map = {}

    def levelorder(self, root, depth):

        queue = collections.deque()
        queue.append(root)
        res = 0
        level = 0

        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                if level == depth:
                    res += 1
                for neighbor in node.childs:
                    queue.append(neighbor)
        return res

    def levelPrint(self, root):

        queue = collections.deque()
        queue.append(root)
        res = []
        level = 0

        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                node = queue.popleft()
                res.append(node.node_str)
                for neighbor in node.childs:
                    queue.append(neighbor)
        return res

    def mergeTree(self, root):

        if not root:
            return

        node = root
        len_child = len(node.childs)

        if len_child == 1:
            node.node_str = node.node_str + "/" + node.childs[0].node_str
            node.childs = node.childs[0].childs
            self.mergeTree(node)
        else:
            for child in node.childs:
                self.mergeTree(child)

    def get_nodes_num(self, org_tree: List[Tuple[str]], depth: int) -> int:

        # 创建树
        for parent, child in org_tree:
            if parent not in self.node_map:
                self.node_map[parent] = Node(parent)
            if child not in self.node_map:
                self.node_map[child] = Node(child)
            self.node_map[parent].childs.append(self.node_map[child])

        print("before:", self.levelPrint(self.node_map["root"]))
        # 开始收缩树
        self.mergeTree(self.node_map["root"])

        print("after:", self.levelPrint(self.node_map["root"]))

        return self.levelorder(self.node_map["root"], depth)  # 累计depth树的深度


org_tree = [
    ["root", "B"],
    ["root", "F"],
    ["C", "E"],
    ["B", "C"],
    ["E", "N"],
    ["F", "H"],
    ["F", "X"],
    ["E", "M"],
    ["X", "i"]]

depth = 3

print(Solution().get_nodes_num(org_tree, depth))
