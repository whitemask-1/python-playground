# This is my original solution to the Valid Anagram problem on LeetCode.
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# My solution involves converting the second string into a list to allow for letter removal as I check each letter in the first string.
# If a letter from the first string is found in the list of the second string, it is removed from the list.
# If a letter is not found, the function returns false.
# If all letters are found and removed, the function returns true.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_list = list(t)
        for letter in s:
            if letter in t_list:
                t_list.remove(letter)
            elif not t:
                return True
            else:
                return False
        return True
    
# Time complexity: O(n^2) in the worst case due to the 'in' check and 'remove' operation within a loop
# Space complexity: O(n) due to the list conversion of string t

#Heres the faster solution using the sorted function
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

# Time complexity: O(n log n) due to the sorting operation
# Space complexity: O(n) due to the space used by the sorted function

# Here is another solution that improves time complexity by using the remove method directly
# Basically just a refinement of my original approach with less unnecessary checks
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_t = list(t)
        for i in s:
            try:
                list_t.remove(i)
            except:
                return False
        return True