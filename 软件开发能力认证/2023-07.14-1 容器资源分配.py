from typing import List


class Solution:
    def get_least_vm_num(self, cpu_core: int, service_a: List[int], service_b: List[int]) -> int:
        
        return 0


if __name__ == "__main__":
    cpu_core, num_a, num_b = list(map(int, "32 3 2".strip().split()))
    service_a = list(map(int, "16 8 16".strip().split()))
    service_b = list(map(int, "2 7".strip().split()))
    function = Solution()
    results = function.get_least_vm_num(cpu_core, service_a, service_b)
    print(results)