from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []

        if not root: return res

        node = root
        stack = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left  # # 到叶子结点时候为None，跳出循环

            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res
