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


def binary_search2_left(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid

    if nums[l] == target:
        return l

    return -1


def binary_search2_right(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        mid = l + (r - l + 1) // 2
        if target < nums[mid]:
            r = mid - 1
        else:
            l = mid

    if nums[r] == target:
        return r

    return -1


sorted_list = [1, 2, 3, 4, 7, 9, 10]
print("binary_search1:        target= 9,  idx=", binary_search1(sorted_list, 9))
print("binary_search2_left:   target= 9,  idx=", binary_search2_left(sorted_list, 9))
print("binary_search2_right:  target= 9,  idx=", binary_search2_right(sorted_list, 9))
