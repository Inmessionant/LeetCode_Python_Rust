class Entity:
    def __init__(self, date, storageId, storageType, storageDays, price, cost):
        self.date = date
        self.storageId = storageId
        self.storageType = storageType
        self.storageDays = storageDays
        self.price = price
        self.cost = cost


class StorageSystem:
    def __init__(self, cold_storage_num: int, cold_storage_price: int, normal_storage_num: int,
                 normal_storage_price: int, delay: int):

        self.store_info = {
            0: [cold_storage_num, cold_storage_price],  # cold number, cold price
            1: [normal_storage_num, normal_storage_price]
        }
        self.delay = delay
        self.success_put = {}
        self.instorage = {}
        self.cleared = {}

    def store(self, date: int, storage_id: int, storage_type: int, storage_days: int) -> int:

        self.update_storage(date)
        if storage_type == 0:  # cold
            if self.store_info[0][0] > 0:
                self.store_info[0][0] -= 1
                cost = storage_days * self.store_info[0][1]
                self.instorage[storage_id] = Entity(date, storage_id, storage_type, storage_days, self.store_info[0][1],
                                                    cost)
                return cost
            return -1
        else:  # noranal
            if self.store_info[1][0] > 0:
                self.store_info[1][0] -= 1
                cost = cost = storage_days * self.store_info[1][1]
                self.instorage[storage_id] = Entity(date, storage_id, storage_type, storage_days, self.store_info[1][1],
                                                    cost)
                return cost
            elif self.store_info[1][0] == 0 and self.store_info[0][0] > 0:
                self.store_info[0][0] -= 1
                cost = storage_days * self.store_info[0][1]
                self.instorage[storage_id] = Entity(date, storage_id, 0, storage_days, self.store_info[0][1], cost)
                return cost
            return -1

    def retrieve(self, date: int, storage_id: int) -> int:

        if not self.instorage.get(storage_id):  # 可能已经被拿出去了
            return -1
        entity = self.instorage.pop(storage_id)
        self.store_info[entity.storageType][0] += 1
        vaild_date = entity.date + entity.storageDays
        entire_date = vaild_date + self.delay
        # 未过期
        if date <= vaild_date:
            self.success_put[storage_id] = entity
            return 0
        # 过期，但是没有超出delay
        elif vaild_date < date <= entire_date:
            self.success_put[storage_id] = entity
            need_to_cost = (date - vaild_date) * entity.price
            return need_to_cost
        # 过期且超出delay
        elif date > entire_date:
            self.cleared[storage_id] = entity
            return -1

    def query(self, date: int):
        self.update_storage(date)
        return len(self.success_put), len(self.instorage), len(self.cleared)

    def update_storage(self, date):

        for id, entity in list(self.instorage.items()):
            if entity.date + entity.storageDays + self.delay < date:
                del self.instorage[id]
                self.store_info[entity.storageType][0] += 1
                self.cleared[id] = entity


if __name__ == '__main__':
    # test1
    # obj = StorageSystem(2, 2, 1, 1, 2)
    # print(obj.store(0, 1, 0, 2))
    # print(obj.retrieve(3, 1))
    # print(obj.query(3))

    # test2
    obj = StorageSystem(2, 2, 1, 3, 2)
    print(obj.query(0))
    print(obj.store(0, 21, 1, 3))
    print(obj.store(1, 22, 1, 4))
    print(obj.store(1, 23, 0, 2))
    print(obj.query(1))
    print(obj.store(4, 26, 1, 2))
    print(obj.retrieve(5, 21))
    print(obj.store(6, 24, 0, 7))
    print(obj.query(7))
    print(obj.query(8))
    print(obj.retrieve(9, 22))
