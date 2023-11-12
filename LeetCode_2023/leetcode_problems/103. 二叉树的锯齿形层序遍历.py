import collections
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []

        res = []
        node = root

        reversed = True
        queue = collections.deque()
        queue.append(node)

        while queue:

            size = len(queue)
            cur_res = []
            reversed = not reversed

            for _ in range(size):
                node = queue.popleft()
                cur_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if reversed:
                cur_res = cur_res[::-1]

            res.append(cur_res)

        return res

