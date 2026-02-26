def reverse(x: int) -> int:
    abs_x = abs(x)
    list_x = [int(a) for a in str(abs_x)]

    reverse_list = list_x[::-1]

    reversed_int = int("".join([str(i) for i in reverse_list]))

    if reversed_int > 2**31 - 1 or reversed_int < -(2**31):
        return 0

    if "-" in str(x):
        reversed_int = -reversed_int
        return reversed_int

    return reversed_int


test = 123
test1 = -421
test2 = 173483293489

print(reverse(test))
print(reverse(test1))
print(reverse(test2))
