import random

coin = random.choice(
    ["heads", "tails"]
)  # Assigns a random value from the list to the coin variable
print(coin)

number = random.randint(1, 10)  # Assigns a Random Int between the specified range
print(number)

cards = ["jack", "king", "queen"]
random.shuffle(cards)
for card in cards:
    print(card)
