# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(node):
            if not node or node.val == None:
                return

            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        res = []
        preorder(root)

        return res


root = [3, 9, 20, None, None, 15, 7]
# 创建每个node, 此时None也会被创建为一个节点，TreeNode(val=None), 后续输出时候要
# 判断if node and node.val != None
nodes = [TreeNode(val=i) for i in root]
# 将node连接起来
for i in range(len(nodes) // 2):
    nodes[i].left = nodes[2 * i + 1]
    nodes[i].right = nodes[2 * i + 2]

print(Solution().preorderTraversal(nodes[0]))  # 传进去是nodes[0]
