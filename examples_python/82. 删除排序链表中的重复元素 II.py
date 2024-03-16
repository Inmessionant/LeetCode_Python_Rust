# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        dummy_node = ListNode(next=head)
        prev, curv = dummy_node, dummy_node.next

        while curv:
            while curv.next and curv.val == curv.next.val:
                curv = curv.next

            if prev.next != curv:
                prev.next = curv.next

            else:
                prev = prev.next

            curv = curv.next

        return dummy_node.next
