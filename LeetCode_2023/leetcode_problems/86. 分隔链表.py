class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #  只需维护两个链表,将小于 x 的节点，放到一个链表；将大于等于 x 的节点，放到另外一个链表，最后连接这两个链表；
        if not head or not head.next:
            return head

        dummy1, dummy2 = ListNode(), ListNode()
        cur1, cur2, cur = dummy1, dummy2, head

        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next

        cur1.next = dummy2.next
        cur2.next = None

        return dummy1.next