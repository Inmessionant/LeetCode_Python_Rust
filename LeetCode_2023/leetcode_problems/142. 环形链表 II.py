from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next: return

        slow = fast = head

        while True:
            if not fast or not fast.next:
                return

            slow, fast = slow.next, fast.next.next

            if slow == fast:
                break

        fast = head

        while fast != slow:
            slow, fast = slow.next, fast.next

        return slow