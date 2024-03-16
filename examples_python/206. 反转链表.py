# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        prev, curv = None, head

        while curv:
            temp = curv.next
            curv.next = prev
            prev = curv
            curv = temp

        return prev
