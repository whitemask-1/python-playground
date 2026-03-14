"""
Given integer array prices where prices[i] is the price on the ith day
    - Need a loop to pick the ith day in prices

choose a single day to buy one price and a day in the future to sell
    - Find the highest value ahead of the current ith day in the loop
    - If there is no value higher than the current ith day
        - then continue the loop and skip the day
    - At the end of the function
        - we need to return 0 if nothing is entered to the current highest variable



"""


def maxprofit(prices: list[int]) -> int:
    current_highest = 0
    i = 0
    while i < len(prices):
        current_day_price = prices[i]
        future_highest = max(prices[i:])
        gain = future_highest - current_day_price
        if gain > current_highest:
            current_highest = gain

        i += 1

    return current_highest


prices = [10, 1, 5, 6, 7, 1]

print(maxprofit(prices))
