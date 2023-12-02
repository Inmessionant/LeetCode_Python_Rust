from typing import List

class Process():

    def __init__(self, processid, occupied, requested):

        self.processid = processid

        self.occupied = occupied

        self.requested = requested


class Solution:

    def deadlock_processes(self, processes: List[Process]) -> List[int]:
        ...

