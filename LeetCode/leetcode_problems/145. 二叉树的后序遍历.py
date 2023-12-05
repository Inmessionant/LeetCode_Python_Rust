from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        if not root: return res

        node = root
        stack = []

        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.right

            node = stack.pop()
            node = node.left

        return res[::-1]
