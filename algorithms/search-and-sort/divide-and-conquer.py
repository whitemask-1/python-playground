# The divide and conquer paradigm is a technique for recursively breaking down problems into smaller sub-problems
# One of the keys aspects of this is recursion which is when a function calls itself repeatedly until a base case is reached

def divide_and_conquer(arr, target):
    # Base case: if the array is empty, return -1 (not found)
    if len(arr) == 0:
        return -1

    mid = len(arr) // 2

    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search in the left half
    elif target < arr[mid]:
        return divide_and_conquer(arr[:mid], target)
    # If the target is greater than the middle element, search in the right half
    else:
        result = divide_and_conquer(arr[mid + 1:], target)
        # If found in the right half, adjust the index to account for the left half
        return result + mid + 1 if result != -1 else -1
    
# Time complexity: O(log n)
# Space complexity: O(log n) due to recursive call stack
# Ok well thats good for searching I guess but Id still rather use binary search for space efficiency
# What else can we do with divide and conquer?

# Sorting is another common application of divide and conquer
# Merge sort is a classic example of a divide and conquer sorting algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Time complexity: O(n log n)
# Space complexity: O(n)