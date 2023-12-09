import collections
from typing import List


class Port:
    def __init__(self, port, pid, packet=0):
        self.port = port
        self.pid = pid
        self.packet = packet


class FlowStatsSystem:
    def __init__(self):
        self.process_map = collections.defaultdict(list)  # (pid, [Port])
        self.pid_packet = collections.defaultdict(int)
        self.port = dict()  # (port_id, Port)
        self.not_bind = dict()  # not used

    def bind_port(self, pid: int, port: int) -> bool:
        if port in self.port:
            return False
        else:
            cur_port = Port(port, pid)
            self.process_map[pid].append(cur_port)
            self.port[port] = cur_port
            return True

    def unbind_port(self, port: int) -> bool:
        if port in self.port:
            cur_port = self.port[port]
            self.process_map[cur_port.pid].remove(cur_port)
            self.port.pop(port)
            self.not_bind[port] = cur_port
            return True
        else:
            return False

    def recv_packet(self, port: int, packet_len: int) -> int:
        if port in self.port:
            cur_pid = self.port[port].pid
            self.pid_packet[cur_pid] += packet_len
            return self.pid_packet[cur_pid]
        else:
            return 0

    def stat_packet(self, top_num: int) -> List[int]:

        top = []
        for key, value in self.pid_packet.items():
            if value == 0:
                continue
            top.append([value, key])
        top.sort(key=lambda x: [-x[0], x[1]])
        top = top[:top_num]
        res = []

        for t in top:
            res.append(t[1])

        return res
