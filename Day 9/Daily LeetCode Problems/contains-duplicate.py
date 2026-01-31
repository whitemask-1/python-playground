from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_cache = []
        for num in nums:
            if num in num_cache:
                return True
            num_cache.append(num)
        return False
    
# I solved the Contains Duplicate problem pretty quickly using a list to keep track of seen numbers.
# Given an integer array nums, return true if any value appears at least twice in the array
# and return false if every element is distinct.
# Time complexity: O(n^2) in the worst case due to the 'in' check within a loop
# Space complexity: O(n) due to the additional list used for caching
