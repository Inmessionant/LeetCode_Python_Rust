# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getListMid(self, head) -> ListNode:

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def listsMerge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode()
        curv = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                curv.next = list1
                list1 = list1.next
            else:
                curv.next = list2
                list2 = list2.next
            curv = curv.next

        curv.next = list1 if list1 else list2

        return dummy_node.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        list_mid = self.getListMid(head)

        list1, list2 = head, list_mid.next
        list_mid.next = None

        list1 = self.sortList(list1)
        list2 = self.sortList(list2)

        return self.listsMerge(list1, list2)




