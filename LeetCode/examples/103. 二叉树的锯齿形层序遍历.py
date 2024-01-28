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
                if node.left and node.left.val != None:
                    queue.append(node.left)
                if node.right and node.right.val != None:
                    queue.append(node.right)

            if reversed:
                cur_res = cur_res[::-1]

            res.append(cur_res)

        return res


root = [3, 9, 20, None, None, 15, 7]
nodes = [TreeNode(val=i) for i in root]
for i in range(len(nodes) // 2):
    nodes[i].left = nodes[2 * i + 1]
    nodes[i].right = nodes[2 * i + 2]

print(Solution().zigzagLevelOrder(nodes[0]))
