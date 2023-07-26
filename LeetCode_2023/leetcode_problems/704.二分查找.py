from typing import List


def binary_search1(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


sorted_list = [1, 2, 3, 4, 7, 9, 10]
print("target= 9, idx=", binary_search1(sorted_list, 9))
