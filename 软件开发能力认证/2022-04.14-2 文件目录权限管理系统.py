import collections
from typing import List


class Node:
    def __init__(self, id):
        self.id = id
        self.status = 1
        self.child = []
        self.owner = []


class DirPermSystem:

    def __init__(self, path: List[int], statuses: List[int]):

        self.node_map = {}

        for idx, parent in enumerate(path):
            if idx not in self.node_map:
                self.node_map[idx] = Node(idx)
            if parent not in self.node_map:
                self.node_map[parent] = Node(parent)
            self.node_map[parent].child.append(self.node_map[idx])

        for i in range(len(statuses)):
            self.node_map[i].status = statuses[i]

    def change_status(self, dir_id: int, status: int) -> None:

        if dir_id in self.node_map:
            self.node_map[dir_id].status = status

    def grant_right(self, user_id: int, dir_id: int) -> None:

        if dir_id not in self.node_map:
            return

        queue = collections.deque()
        queue.append(self.node_map[dir_id])

        while queue:
            node = queue.popleft()
            node.owner.append(user_id)

            for child in node.child:
                queue.append(child)

    def remove_right(self, user_id: int, dir_id: int) -> bool:
        if user_id in self.node_map[dir_id].owner:
            self.node_map[dir_id].owner.remove(user_id)
            return True
        return False

    def query_right(self, user_id: int, dir_id: int) -> bool:

        if dir_id not in self.node_map:
            return False

        if self.node_map[dir_id].status == 1:
            return True
        elif self.node_map[dir_id].status == 2 and user_id in self.node_map[dir_id].owner:
            return True

        return False

    def query_num(self, user_id: int) -> int:

        res = []

        queue = collections.deque()
        queue.append(self.node_map[0])

        while queue:
            node = queue.popleft()

            if node.status == 1 or (node.status == 2 and user_id in node.owner):
                res.append(node)
            for child in node.child:
                if child:
                    queue.append(child)

        return len(res)


path = [-1, 4, 4, 1, 0]
statuses = [1, 1, 2, 1, 1]
obj = DirPermSystem(path, statuses)
print(obj.grant_right(101, 1))
print(obj.change_status(1, 2))
print(obj.query_right(101, 3))
print(obj.query_num(101))
print(obj.remove_right(101, 1))
