import typing


def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    left = 0
    longest = 0

    for idx, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = idx
        longest = max(longest, idx - left + 1)

    return longest


test = "dvdfgds"
print(lengthOfLongestSubstring(test))
