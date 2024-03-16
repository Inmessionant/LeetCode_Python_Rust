# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        new_head = head
        # 找到下一组k的起始位置，如果小于k个直接返回head,不需要翻转
        for _ in range(k):
            if not new_head:  return head
            new_head = new_head.next

        # 翻转k个
        prev, curv = None, head
        while curv != new_head:
            temp = curv.next
            curv.next = prev
            prev = curv
            curv = temp

        new_head = prev
        # 递归下一组k个链表翻转，并连接到head.next
        head.next = self.reverseKGroup(curv, k)

        return new_head
