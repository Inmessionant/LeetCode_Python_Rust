# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []  # heapq默认最小堆

        for s in lists:
            while s:
                heapq.heappush(min_heap, s.val)
                s = s.next

        dummy_node = ListNode()
        prev = dummy_node

        while min_heap:
            curv = ListNode(heapq.heappop(min_heap))
            prev.next = curv
            prev = prev.next

        return dummy_node.next
