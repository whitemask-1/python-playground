def dailyTemperatures(temperatures: list(int)) -> list(int):
    res = [0] * len(temperatures)
    stack = [] #Use pairs (temp, index)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t, i))

    return res


def dayTemps(temperatures: list(int)) -> list(int):
    result = []
    for idx, temp in enumerate(temperatures):
        hottest_idx, next_hottest = next(((i, t) for i, t in enumerate(temperatures) if i >= idx and t > temp), (None, None))
        if not next_hottest or not hottest_idx:
            result.append(0)
            continue
        result.append(hottest_idx - idx)

    return result

temps = [30,38,30,36,35,40,28]
print(dailyTemperatures(temps))
print(dayTemps(temps))

