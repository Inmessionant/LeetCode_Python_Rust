import heapq
from typing import List


class Solution:
    def get_least_vm_num(self, cpu_core: int, service_a: List[int], service_b: List[int]) -> int:

        res = 0

        min_heap = service_a.copy()
        heapq.heapify(min_heap)

        for cur_service in sorted(service_b, reverse=True):
            if not min_heap or cur_service + min_heap[0] > cpu_core:
                heapq.heappush(min_heap, cur_service)
            else:
                heapq.heappop(min_heap)
                res += 1

        return res + len(min_heap)


if __name__ == "__main__":
    cpu_core, num_a, num_b = list(map(int, "32 3 2".strip().split()))
    service_a = list(map(int, "16 8 16".strip().split()))
    service_b = list(map(int, "2 7".strip().split()))
    function = Solution()
    results = function.get_least_vm_num(cpu_core, service_a, service_b)
    print(results)