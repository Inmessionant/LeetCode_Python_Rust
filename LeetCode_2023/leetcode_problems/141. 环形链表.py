# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not  head.next: return False

        slow = fast = head

        while True:

            if not fast or not fast.next:
                return False

            slow, fast = slow.next, fast.next.next

            if slow == fast:
                return True
