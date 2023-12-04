import collections
from pprint import pprint
from typing import List, Tuple


class Solution:
    def getAcount(self, ops):
        data_stat, write_stat = collections.defaultdict(list), collections.defaultdict(list)

        for idx, thread in enumerate(ops):
            for op in thread:
                if op[0] == "lock" or op[0] == "unlock":
                    continue
                cur_op, data = op[0], op[1]
                if idx not in data_stat[data]:
                    data_stat[data].append(idx)
                if cur_op == "write" and idx not in write_stat[data]:
                    write_stat[data].append(idx)
        # pprint(data_stat)
        # pprint(write_stat)
        return data_stat, write_stat

    def get_data_races(self, thread_ops: List[List[Tuple[str, str]]]) -> List[str]:
        data_stat, write_stat = self.getAcount(thread_ops)
        res = []

        for thread_idx, thread_op in enumerate(thread_ops):
            locked = False
            for cur_op in thread_op:
                if cur_op[0] == "lock":
                    locked = True
                    continue
                elif cur_op[0] == "unlock":
                    locked = False
                    continue
                cur_op, data = cur_op[0], cur_op[1]
                if data in res:
                    continue
                if len(data_stat[data]) > 1 and len(write_stat[data]) > 0 and not locked and \
                    ((cur_op == "write") or  # 线程 A 中该写操作未获得锁 + 其它线程（B …）的任一写未获得锁
                     (thread_idx not in write_stat[data])):  # 其它线程（B …）的任一读未获得锁
                    res.append(data)

        return sorted(res)


thread_ops = [
    [["read", "para"], ["write", "msg"], ["read", "para"], ["write", "port"], ],
    [["write", "port"], ["lock"], ["read", "msg"], ["unlock"], ["write", "buff"], ["read", "buff"], ["read", "para"]]
]

thread_ops = [
    [["lock"],  ["read", "a"], ["write", "a"], ["unlock"]],
    [["lock"],  ["read", "a"], ["unlock"], ["read", "a"], ["write", "b"], ["read", "b"]],
    [["lock"],  ["write", "a"], ["unlock"]]
]
print(Solution().get_data_races(thread_ops))
