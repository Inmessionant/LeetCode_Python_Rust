# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root: return res

        node = root
        stack = []

        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left  # 到叶子结点时候为None，跳出循环

            node = stack.pop()  # 上一个node
            node = node.right

        return res