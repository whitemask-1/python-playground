# There are two key algorithms to know when it comes to searching: linear search and binary search

# Linear starts at the beginning of a list and iterates until it finds the target
# If the target value is found the index is returned, otherwise -1 is returned
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Time complexity: O(n)
# Space complexity: O(1)

# Binary search is more efficient but requires a sorted list in ascending order
# It works by dividing the list in halves and checking if the target value is in the middle
# If the target is less than the middle value, it continues searching in the left half
# If the target is greater than the middle value, it continues searching in the right half
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Time complexity: O(log n)
# Space complexity: O(1)