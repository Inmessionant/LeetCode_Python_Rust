# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val, level, left=None, right=None):
        self.val = val
        self.level = level
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.node_map = collections.defaultdict(list)
        root = TreeNode(-1, 0)
        self.node_map[0].append(root)

    def create_tree(self, operations: List[List[int]]) -> Optional[TreeNode]:

        for idx in range(len(operations)):
            cur_level, cur_idx = operations[idx][0], operations[idx][1]
            node = self.node_map[cur_level][cur_idx]

            if not node.left:
                cur_node = TreeNode(idx, cur_level + 1)
                node.left = cur_node
                self.node_map[cur_level + 1].append(cur_node)

            elif not node.right:
                cur_node = TreeNode(idx, cur_level + 1)
                node.right = cur_node
                self.node_map[cur_level + 1].append(cur_node)

        return self.node_map[0][0]

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root: return res

        queue = collections.deque()
        queue.append(root)
        level = 0  # 存储层数

        while queue:
            size = len(queue)  # 当前层数节点数量
            level += 1  # 当前层有节点，level + 1
            cur_res = []  # 临时变量，记录当前层的节点
            for _ in range(size):  # 遍历某一层的节点
                node = queue.popleft()  # 将要处理的节点弹出
                cur_res.append(node.val)
                # 如果当前节点有左右节点，则压入队列，根据题意注意压入顺序，先左后右
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_res)  # 某一层的节点都处理完之后，存入res

        return res


operations = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 1], [2, 0], [3, 1], [2, 0]]
obj = Solution()
node = obj.create_tree(operations)
print(obj.levelOrder(node))
