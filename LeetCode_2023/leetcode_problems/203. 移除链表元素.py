from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head: return head

        dummy_node = ListNode(next=head)
        cur_node = dummy_node

        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next

        return dummy_node.next
