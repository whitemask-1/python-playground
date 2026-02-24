def longestCommonPrefix(strs):
    result = ""

    if not strs:
        return result

    strs_s = sorted(strs)
    first = strs_s[0]
    last = strs_s[-1]

    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            result += first[i]
            pass
        else:
            break

    return result


test_list = ["florida", "flame", "flounder"]
print(longestCommonPrefix(test_list))
