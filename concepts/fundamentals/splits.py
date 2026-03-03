string = "the-biggest_bird"
list_str = string.replace("_", "-").split("-")
result = list_str.pop(0) + "".join([x.capitalize() for x in list_str])
print(result)
