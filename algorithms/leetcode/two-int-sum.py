"""
Given an array of numbers sorted in increasing order

return the indices of two numbers such that they add up to a target number and index1 < index2
    - index1 and index2 cannot be equal

Always exactly one valid solution
Must be O(1) space complexity

Approach:
    - For every i in the range of the num array
    - We can use left and right to point at the first num in the array and the last num in the array
    - Note that this is a searching problem
        - we can use binary search to search through the array for a complement to target - nums[i]
        - so while our i pointer is at a value less than the j pointers value
            - find the middle of the number array ahead of i
                - if the middle num is the complement we return i
                - if its less than the complement we move the left pointer to the middle value + 1
                - else move our right side pointer to middle - 1

    - If no pair is found just return an empty array
"""

def twoSum(numbers: list[int], target: int) -> list(int):
    for i in range(len(numbers)):
        left, right = i + 1, len(numbers) - 1
        complement = target - numbers[i]
        while left <= right:
            middle = left + (right - left) // 2
            if numbers[middle] == complement:
                return [i + 1, middle + 1]
            elif numbers[middle] < complement:
                left = middle + 1
            else:
                right = middle - 1

    return []

numbers = [1,2,3,4]
target = 3
print(twoSum(numbers, target))
