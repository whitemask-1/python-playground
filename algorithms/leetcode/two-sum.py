from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            indices = []
            indices.append(i)
            finder = target - num
            if finder in nums[i+1:]:
                finder_index = nums.index(finder, i+1)
                indices.append(finder_index)
                sort_indices = sorted(indices)
                return sort_indices
            
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Originally when solving it was pretty straightforward, but I had some issues with getting the correct indices when there were duplicate numbers in the list.
# I tried removing the first occurrence of the number from the list to avoid getting the same index, but that messed up the indexing.
# The final solution I came up with was to manipulate the starting index of the search for the second number using slicing and the index method's start parameter.
# Time complexity: O(n^2) in the worst case due to the 'in' check within a loop
# Space complexity: O(1)