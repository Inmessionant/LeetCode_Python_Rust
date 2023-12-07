from typing import List


class Room:
    def __init__(self, id: int, area: int, price: int, rooms: int, address: List[int], dist=0):
        self.id = id
        self.area = area
        self.price = price
        self.rooms = rooms
        self.address = address
        self.dist = dist


class RentingSystem:

    def __init__(self):
        self.room_map = {}

    def add_room(self, id: int, area: int, price: int, rooms: int, address: List[int]) -> bool:

        if id not in self.room_map:
            self.room_map[id] = Room(id, area, price, rooms, address)
            return True
        else:
            cur_room = self.room_map[id]
            cur_room.area = area
            cur_room.price = price
            cur_room.rooms = rooms
            cur_room.address = address
            return False

    def delete_room(self, id: int) -> bool:
        if id in self.room_map:
            self.room_map.pop(id)
            return True
        else:
            return False

    def query_room(self, area: int, price: int, rooms: int, address: List[int], order_by: List[List[int]]) -> List[int]:

        availd_rooms = []  # id, area, price, rooms, address, dist

        for key, value in self.room_map.items():
            if value.area >= area and value.price <= price and value.rooms == rooms:
                dist = abs(address[0] - value.address[0]) + abs(address[1] - value.address[1])
                availd_rooms.append([value.id, value.area, value.price, dist])

        order_by.append([0, 1])  # default order: id

        availd_rooms.sort(key=lambda x: [x[order[0]] * order[1] for order in order_by])

        return [room[0] for room in availd_rooms]


obj = RentingSystem()

# case1
# print(obj.add_room(3, 24, 200, 2, [0, 1]))
# print(obj.add_room(1, 10, 400, 2, [1, 0]))
# print(obj.query_room(1, 400, 2, [1, 1], [[3, 1], [2, -1]]))
# print(obj.delete_room(3))

# case2
print(obj.delete_room(10))
print(obj.add_room(3, 24, 200, 2, [0, 1]))
print(obj.add_room(3, 24, 500, 2, [0, 1]))
print(obj.add_room(3, 27, 500, 4, [1, 1]))
print(obj.add_room(1, 27, 500, 4, [20, 43]))
print(obj.add_room(6, 35, 227, 4, [2, 4]))
print(obj.add_room(9, 20, 3540, 4, [4, 321]))
print(obj.query_room(25, 900, 4, [10, 1], [[1, 1], [2, -1], [3, 1]]))
print(obj.query_room(25, 900, 4, [10, 1], []))
