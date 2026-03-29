tf = (1, 5, (0,1))
tm = (1, 5, [0,1])
def fixed(x: tuple) -> bool:
    try:
        hash(x)
        return True
    except TypeError:
        return False

print(fixed(tf))
print(fixed(tm))
