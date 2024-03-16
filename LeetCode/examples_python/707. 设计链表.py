class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):

        self.head = ListNode()  # dummy_node
        self.count = 0

    def get(self, index: int) -> int:

        if index >= self.count: return -1

        node = self.head.next

        for _ in range(index):
            node = node.next

        return node.val

    def addAtHead(self, val: int) -> None:

        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:

        return self.addAtIndex(self.count, val)

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.count:  return  # 如果 index 比长度更大，该节点将 不会插入 到链表中

        self.count += 1

        add_node = ListNode(val)

        pre, cur = self.head, self.head.next

        for _ in range(index):
            pre, cur = pre.next, cur.next

        # cur位置在index
        pre.next, add_node.next = add_node, cur

    def deleteAtIndex(self, index: int) -> None:

        if index >= self.count:
            return

        self.count -= 1
        pre, cur = self.head, self.head.next

        for _ in range(index):
            pre, cur = pre.next, cur.next

        # cur位置在index
        pre.next = cur.next
