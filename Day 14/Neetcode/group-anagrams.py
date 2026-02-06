def group_anagrams(strs):
    anagram_dict = {}
    while strs:
        word = strs.pop()
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict.keys():
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return list(anagram_dict.values())

# Example usage
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_strs))
# Output: [['bat'], ['nat', 'tan'], ['ate', 'tea', 'eat']]

