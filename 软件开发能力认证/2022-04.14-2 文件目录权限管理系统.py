import collections
from typing import List


class Node:
    def __init__(self, id, status=1):
        self.id = id
        self.status = status
        self.child = []


class DirPermSystem:

    def __init__(self, path: List[int], statuses: List[int]):
        self.user_dirs = collections.defaultdict(list)
        self.node_map = {}

        for idx, parent in enumerate(path):
            if idx not in self.node_map:
                curnode = Node(idx)
                self.node_map[idx] = curnode
            if parent not in self.node_map:
                parent_node = Node(parent)
                self.node_map[parent] = parent_node
            self.node_map[parent].child.append(curnode)

            # print("==========", idx)
            # print(self.node_map[idx].id, self.node_map[parent].id)

        for i in range(len(statuses)):
            self.node_map[i].status = statuses[i]

        # for key, value in self.node_map.items():
        #     print("key=", key)
        #     for child in value.child:
        #         print("child： ", child.id)

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
            self.user_dirs[user_id].append(node)

            for child in node.child:
                queue.append(child)

    def remove_right(self, user_id: int, dir_id: int) -> bool:
        if user_id in self.user_dirs and self.node_map[dir_id] in self.user_dirs[user_id]:
            self.user_dirs[user_id].remove(self.node_map[dir_id])
            return True
        return False

    def query_right(self, user_id: int, dir_id: int) -> bool:

        if dir_id not in self.node_map:
            return False

        if self.node_map[dir_id].status == 1:
            return True

        if user_id not in self.user_dirs:
            return False

        for node in self.user_dirs:
            if dir_id == node.id:
                return True

        return False

    def query_num(self, user_id: int) -> int:

        if user_id not in self.user_dirs:
            return 0

        return len(self.user_dirs[user_id])


path = [-1, 4, 4, 1, 0]
statuses = [-1, 4, 4, 1, 0]
obj = DirPermSystem(path, statuses)
print(obj.grant_right(101, 1))
print(obj.change_status(1, 2))
print(obj.query_right(101, 3))
print(obj.query_num(101))
print(obj.remove_right(101, 1))
