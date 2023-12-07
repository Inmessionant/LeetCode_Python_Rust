from typing import List


class RentingSystem:

    def __init__(self):
        ...

    def add_room(self, id: int, area: int, price: int, rooms: int, address: List[int]) -> bool:
        ...

    def delete_room(self, id: int) -> bool:
        ...

    def query_room(self, area: int, price: int, rooms: int, address: List[int], order_by: List[List[int]]) -> List[int]:
        ...


obj = RentingSystem()
print(obj.add_room(3, 24, 200, 2, [0, 1]))
print(obj.add_room(1, 10, 400, 2, [1, 0]))
print(obj.query_room(1, 400, 2, [1, 1], [[3, 1], [2, -1]]))
print(obj.delete_room(3))
