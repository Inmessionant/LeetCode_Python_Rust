# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def create_tree(self, operations: List[List[int]]) -> Optional[TreeNode]:
        ...
