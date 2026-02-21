def isPalindrome(num):
    s = str(num)
    return s == s[::-1]


# This is ultimately the best solution with the fastest time completion and the second least number of lines (possible with only a single line of code)

print(isPalindrome(161))

# This is my original solution to the problem, figuring out how to handle the index was interesting, and doing it
# without the [::-1] is honestly an accomplishment


def complexIsPalindrome(num):
    s = str(num)

    for idx, i in enumerate(s):
        if i != s[-idx - 1]:
            return False

    return True


print(complexIsPalindrome(14513))
print(complexIsPalindrome(15651))


# One-liner
def singlelinePalindrome(num):
    return str(num) == str(num)[::-1]


print(singlelinePalindrome(1389831))
print(singlelinePalindrome(128523))
