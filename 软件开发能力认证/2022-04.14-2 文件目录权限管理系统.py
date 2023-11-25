from typing import List


class DirPermSystem:

    def __init__(self, path: List[int], statuses: List[int]):
        ...

    def change_status(self, dir_id: int, status: int) -> None:
        ...

    def grant_right(self, user_id: int, dir_id: int) -> None:
        ...

    def remove_right(self, user_id: int, dir_id: int) -> bool:
        ...

    def query_right(self, user_id: int, dir_id: int) -> bool:
        ...

    def query_num(self, user_id: int) -> int:
        ...

path = [-1, 4, 4, 1, 0]
statuses = [-1, 4, 4, 1, 0]
obj = DirPermSystem(path, statuses)
