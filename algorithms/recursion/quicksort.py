# The quick sort algorithms works by selecting an item in the list called a pivot.
# The the list is partitioned into two sublists (less than the pivot and greater than the pivot) based on the pivot item and then the sublists are sorted recursively.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
    
# The quicksort algorithm will work no matter what item is selected as the pivot but some choices are better than others
# When partitioning, two sublists are created and ideally they are of roughly equal size.
# If the pivot is always the smallest or largest item, one sublist will be empty and the other will contain all the other items.
# This results in unbalanced partitions and can lead to poor performance (O(n^2) time complexity) in the worst case.
# Choosing the middle item as the pivot (as done here) is a simple strategy that often leads to more balanced partitions.

print(quicksort([3,6,8,10,1,2,1]))  # Output: [1, 1, 2, 3, 6, 8, 10]
print(quicksort([5,3,7,6,2,9,1,4,8]))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(quicksort([]))  # Output: []
print(quicksort([1]))  # Output: [1]
print(quicksort([2,1]))  # Output: [1, 2]
print(quicksort([1,2,3,4,5]))  # Output: [1, 2, 3, 4, 5]
print(quicksort([5,4,3,2,1]))  # Output: [1, 2, 3, 4, 5]