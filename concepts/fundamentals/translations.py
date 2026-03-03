vowels = "aeiou"
remove_vowel_map = {ord(char): None for char in vowels}

text = "Hello world!, Testing Testing"

translated_text = text.translate(remove_vowel_map)

print(translated_text)


## of course someone else made understands translate way better than me and does the same thing with
def disemvowel(string):
    return string.translate(None, "aAeEuUoOiI")


print(disemvowel(text))  # JUST KIDDING translate() only takes one argument HAHAHAHAHAHA
