# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root: return True

        depth_root, is_balance_root = self.isVaild(root)

        return is_balance_root

    def isVaild(self, node):

        if not node:
            return 0, True

        depth1, isBalance1 = self.isVaild(node.left)
        depth2, isBalance2 = self.isVaild(node.right)

        return max(depth1, depth2) + 1, isBalance1 and isBalance2 and abs(depth1 - depth2) <= 1
