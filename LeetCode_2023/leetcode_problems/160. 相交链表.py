from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        node_a, node_b = headA, headB

        while node_a != node_b:
            node_a = node_a.next if node_a else headB
            node_b = node_b.next if node_b else  headA

        return node_a
