import random

def guess_random(range: int) -> None:
    random_num = random.randint(0, range)
    while True:
        user_guess = input("Guess the number: ")
        try:
            user_guess = int(user_guess)
            if user_guess == random_num:
                print("Success")
                break
            elif user_guess < random_num:
                print("Too Low")
                continue
            elif user_guess > random_num:
                print("Too High")

        except ValueError as e:
            print(f"{e} is not a valid input")

def play_forever(range: int):
    while True:
        guess_random(range)
        play_again: str = input("Play Again? [y/n] ")
        if play_again == 'y':
            continue
        break

play_forever(99)
