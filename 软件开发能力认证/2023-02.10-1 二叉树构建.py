# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, x, level, left=None, right=None):
        self.val = x
        self.level = level
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.node_map = collections.defaultdict(list)
        root = TreeNode(-1, 0)
        self.node_map[0].append(root)

    def create_tree(self, operations: List[List[int]]) -> Optional[TreeNode]:
        ...
