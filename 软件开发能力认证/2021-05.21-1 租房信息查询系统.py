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