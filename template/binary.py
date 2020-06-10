from typing import List


def binarySearch(arr: List[int], num: int) -> int:
    '''return index'''
    left = 0
    right = len(arr) - 1
    while left <= right:
        # careful: the offset is needed
        mid = left + (right - left) // 2
        if arr[mid] > num:
            right = mid - 1
        elif arr[mid] < num:
            left = mid + 1
        else:
            return mid
    return None


# disable auto update
print(binarySearch([1, 2, 3, 4, 5, 8, 9], 8))
