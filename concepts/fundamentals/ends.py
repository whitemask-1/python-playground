str1 = "string"
str2 = "ing"
str3 = "png"

print(type(str1[: len(str2) - 1 : -1]))
print(type(str2[::-1]))
print(str2[::-1] == str1[: len(str2) - 1 : -1])
