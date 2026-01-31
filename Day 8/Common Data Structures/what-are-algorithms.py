# An algorithm is a set of unambiguous instructions for solving a provlem or carrying out a task
# You can think of an algorithm as a recipe that outlines the steps needed to prepare a dish.

# Algorithsms have two key characteristics:
# 1. Definiteness: Each step of the algorithm must be clearly and unambiguously defined.
# 2. Finiteness: An algorithm must always terminate after a finite number of steps.
# They may have zero, one, or more inputs and produce at least one output.

# The steps of an algorithm are independant of any programming language.
# But to actually make them run on a computer, they need to be implemented in a specific programming language.

# If an algorithm is correct, the output for any valid input will be the expected result.
# In addition to being correct, algorithms are often evaluated based on their efficiency,
# which includes factors like time complexity (how fast they run) and space complexity (how much memory they use).

# As the process grows in size and complexity, if the algorithm is not efficient, it can lead to significant performance issues.
# This is where Big O notation comes into play, providing a way to describe the performance or complexity of an algorithm in terms of input size.

# Big O notation describes the worst-case performance, or growth rate, of an algorithm as the input size increases.
# The growth rate refers to how the time or space requirements of an algorithm change as the size of the input data set increases.

# Big O focuses on the worst-case because this case is important to understand how efficient the algorithm can be, even in worst case, regardless of input

# Common Big O Classifications: (from most to least efficient)
# O(1) - Constant Time: The algorithm's performance is constant and does not change
# O(log n) - Logarithmic Time: The algorithm's performance grows logarithmically as the input size increases
# O(n) - Linear Time: The algorithm's performance grows linearly with the input size
# O(n log n) - Linearithmic Time: The algorithm's performance grows in proportion
# O(n^2) - Quadratic Time: The algorithm's performance grows quadratically with the input size
# O(2^n) - Exponential Time: The algorithm's performance doubles with each
# O(n!) - Factorial Time: The algorithm's performance grows factorially with the input size

#For Big O notation, we denote input size with 'n' and focus on the term that grows the fastest as n increases, ignoring constant factors and lower-order terms.

# Here is an example of each Big O classification:

# O(1) - Constant Time
def get_first_element(arr):
    return arr[0] if arr else None

#How was it calculated?
# The function get_first_element accesses the first element of the array directly, regardless of the size of the array.
# This means that the time it takes to execute this function does not change as the size of the input array increases.
# Therefore, its time complexity is O(1), or constant time.

# O(log n) - Logarithmic Time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#How was it calculated?
# The binary_search function works by repeatedly dividing the search interval in half.
# Each time the function checks the middle element of the current interval, it eliminates half of the remaining elements from consideration.
# This halving process continues until the target element is found or the search interval is empty.
# Because the size of the search space is reduced by half with each iteration, the time complexity of this algorithm is O(log n), or logarithmic time.

# O(n) - Linear Time
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#How was it calculated?
# The linear_search function iterates through each element of the array one by one until it finds the target element or reaches the end of the array.
# In the worst-case scenario, the function may need to check every element in the array to find the target.
# Therefore, the time it takes to execute this function grows linearly with the size of the input array.
# As a result, its time complexity is O(n), or linear time.

# O(n log n) - Linearithmic Time
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

#How was it calculated?
# The merge_sort function implements the merge sort algorithm, which is a divide-and-conquer sorting algorithm.
# The algorithm works by recursively dividing the input array into two halves until each half contains a single element.
# This division process takes O(log n) time because the array is halved at each step.
# After the array is divided, the algorithm then merges the sorted halves back together.
# The merging process involves comparing elements from the two halves and combining them into a single sorted array.
# This merging process takes O(n) time because each element from both halves needs to be examined.
# Therefore, the overall time complexity of the merge sort algorithm is O(n log n), or

# O(n^2) - Quadratic Time
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#How was it calculated?
# The bubble_sort function implements the bubble sort algorithm, which is a simple sorting algorithm.
# The algorithm works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order.
# This process is repeated for each element in the array.
# In the worst-case scenario, the algorithm needs to make n passes through the array, and during each pass, it compares up to n elements.
# Therefore, the total number of comparisons in the worst case is proportional to n * n, which results in a time complexity of O(n^2), or quadratic time.

# O(2^n) - Exponential Time
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#How was it calculated?
# The fibonacci function calculates the nth Fibonacci number using a recursive approach.
# In this implementation, each call to fibonacci(n) results in two additional calls: fibonacci(n-1) and fibonacci(n-2).
# This branching continues until the base cases (n <= 1) are reached.
# As a result, the number of function calls grows exponentially with the input size n.
# Specifically, the number of calls can be approximated by 2^n, leading to a time complexity of O(2^n), or exponential time.

# O(n!) - Factorial Time
def permute(elements):
    if len(elements) == 0:
        return [[]]
    result = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i+1:]
        for p in permute(rest):
            result.append([elements[i]] + p)
    return result

#How was it calculated?
# The permute function generates all permutations of a list of elements using a recursive approach.
# For each element in the list, the function generates all permutations of the remaining elements.
# This results in n recursive calls for a list of length n, and each call generates permutations of a smaller list.
# The total number of permutations of n elements is n!, and the function explores all of them.
# Therefore, the time complexity of this function is O(n!), or factorial time.

# This notation can also be applied to the context of space requirements, where it describes how the memory usage of an algorithm grows with the size of the input data set.
# For example, an algorithm with a space complexity of O(n) requires memory that grows linearly with the input size, while an algorithm with a space complexity of O(1) uses a constant amount of memory regardless of input size.

#Algorithms are the building blocks of computer science and programming.
# They provide systematic methods for solving problems and performing tasks efficiently.
# Understanding algorithms and their complexities is crucial for designing efficient software and systems.
