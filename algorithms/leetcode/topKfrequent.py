def topKFrequent(nums: list(int), k: int) -> list(int):
    frequents_map: dict = {}
    num_set = set(nums)
    for num in num_set:
        frequency = nums.count(num)
        frequents_map[num] = frequency

    sort_frequents = dict(sorted(frequents_map.items(), key=lambda item: item[1], reverse=True))

    return list(sort_frequents.keys())[0:k]

print(topKFrequent([1,2,3,4,3,2,4,5,6], 3))
