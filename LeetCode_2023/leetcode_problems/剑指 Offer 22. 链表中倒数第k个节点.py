# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        for _ in range(k):
            if not fast: return
            fast = fast.next
        while fast:
            fast, slow = fast.next, slow.next
        return slow
