from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def orderTraversal(self, node): # 右 - 中 - 左

        if not node:
            return None

        self.orderTraversal(node.right)

        node.val += self.sum
        self.sum = node.val

        self.orderTraversal(node.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.orderTraversal(root)

        return root
