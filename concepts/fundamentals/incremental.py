def increment(y) -> int:
    if y == 0:
        return 1
    elif y % 2 == 1:
        return 2 * increment(y / 2)
    else:
        return y + 1


odd = 5

print(increment(5))
