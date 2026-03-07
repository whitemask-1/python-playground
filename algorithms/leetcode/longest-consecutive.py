arr: list[int] = [4, 3, 1, 3, 5, 6, 7]


# Find the length of longest consecutive sequence where each element is 1 > than the previous element
def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0
    res = 0
    nums.sort()

    curr, streak = nums[0], 0
    i = 0

    while i < len(nums):
        if curr != nums[i]:
            curr = nums[i]
            streak = 0
        while i < len(nums) and nums[i] == curr:
            i += 1
        streak += 1
        curr += 1
        res = max(res, streak)
    return res


print(longestConsecutive(arr))
