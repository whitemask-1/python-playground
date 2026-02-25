import typing


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    sorted_nums = sorted(nums1 + nums2)
    if len(sorted_nums) % 2 == 1:
        middle = len(sorted_nums) // 2
        return float(sorted_nums[middle])

    if len(sorted_nums) % 2 == 0:
        left_mid = len(sorted_nums) // 2
        right_mid = left_mid + 1
        median = (sorted_nums[left_mid - 1] + sorted_nums[right_mid - 1]) / 2
        return median


test1 = [1, 3, 5, 6]
test2 = [2, 5, 6, 7]

print(findMedianSortedArrays(test1, test2))


# INITIAL REASONING:
# first add the two lists as a single sorted list using a iteration of the mergesort merge function
# find middle index of the list, if the number isnt exactly the middle include the other number to its right since the middle index will be floored
# if there are two numbers add them and divide by two otherwise just return the median as the middle index
