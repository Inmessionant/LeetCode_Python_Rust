import collections
from typing import Tuple, List


class Solution:

    def get_check_points(self, nodes: List[Tuple[int, List[int]]], key_nodes: List[int], org: int) -> List[int]:

        node_dicts = {}

        for node_rel in nodes:
            node_dicts[node_rel[0]] = node_rel[1]

        queue = collections.deque([org])
        key_nodes_to_check = set()

        while queue:
            node = queue.popleft()
            if node not in key_nodes_to_check:
                if node in key_nodes:
                    key_nodes_to_check.add(node)
                for node in node_dicts[node]:
                    queue.append(node)

        # print(key_nodes_to_check)  # [60, 20, 10]

        queue = collections.deque(list(key_nodes_to_check))
        key_nodes_to_check = set()

        while queue:
            node = queue.popleft()
            if node not in key_nodes_to_check:
                key_nodes_to_check.add(node)
                for key, val in node_dicts.items():
                    if node in val and key not in key_nodes_to_check:
                        queue.append(key)

        if org not in key_nodes_to_check:
            key_nodes_to_check.add(org)

        return sorted(list(key_nodes_to_check))


# nodes = [
#     [20, [10]],
#     [10, []],
#     [30, [10, 20]],
#     [60, [20]],
#     [40, [80, 30]],
#     [50, [30]],
#     [80, []]
# ]
#
# key_nodes = [30, 10, 80]
# org = 60

nodes = [
    [5, [3]],
    [1, []],
    [3, [1, 2, 4]],
    [2, [5]],
    [4, [5]]
]

key_nodes = [3]
org = 3
print(Solution().get_check_points(nodes, key_nodes, org))
