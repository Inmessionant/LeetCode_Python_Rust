# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        if not root: return res

        queue = deque()
        queue.append(root)
        level = 0  # 存储层数

        while queue:
            size = len(queue)  # 当前层数节点数量
            level += 1 # 当前层有节点，level + 1
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
