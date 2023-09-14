# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head.next:
            return head

        dummy_node = ListNode(next=head)
        pre_node = dummy_node

        for _ in range(left - 1):
            pre_node = pre_node.next

        prev, curv = None, pre_node.next

        for _ in range(right - left + 1):
            temp = curv.next
            curv.next = prev
            prev = curv
            curv = temp

        pre_node.next.next = curv
        pre_node.next = prev

        return dummy_node.next
