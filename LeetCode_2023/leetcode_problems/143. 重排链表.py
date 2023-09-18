# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeLists(self, l1, l2):

        while l1 and l2:
            l1_next, l2_next = l1.next, l2.next
            l1.next = l2
            l2.next = l1_next
            l1, l2 = l1_next, l2_next

    def reverseList(self, head):

        prev, curv = None, head

        while curv:
            temp = curv.next
            curv.next = prev
            prev = curv
            curv = temp

        return prev

    def getListMidNode(self, head):

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reorderList(self, head: Optional[ListNode]) -> None:  # 找到中点断开，翻转后面部分，然后合并前后两个链表
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next: return

        mid_node = self.getListMidNode(head)

        reversed_list_head = self.reverseList(mid_node)

        self.mergeLists(head, reversed_list_head)