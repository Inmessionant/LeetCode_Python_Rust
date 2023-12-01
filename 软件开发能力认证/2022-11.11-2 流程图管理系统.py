from typing import List


class Node():
    def __init__(self, id, type):
        self.id = id
        self.type = type


class FlowchartSys: # 只保存手工建立的链接，
    def __init__(self):
        self.node_map = dict()
        self.connections = dict()

    def add_node(self, node_id: int, node_type: int) -> bool:

        if node_id not in self.node_map:
            new_node = Node(node_id, node_type)
            self.node_map[node_id] = new_node
            return True
        else:


    def add_connection(self, connect_id: int, start_node_id: int, end_node_id: int) -> bool:
        ...

    def remove_connection(self, connect_id: int) -> bool:
        ...

    def remove_node(self, node_id: int) -> bool:
        ...

    def query(self, node_id: int) -> List[int]:
        ...


obj = FlowchartSys()
print(obj.add_node(100, 0))
print(obj.add_node(101, 0))
print(obj.add_node(102, 1))
print(obj.add_connection(20, 100, 101))
print(obj.add_node(105, 1))
print(obj.query(100))
print(obj.remove_node(100))
print(obj.add_connection(20))
