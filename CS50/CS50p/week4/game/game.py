import random
import sys


def main():
    while True:
        level = input("Level: ")
        if is_p_int(level):
            target = random.randint(1, int(level))
            break

    while True:
        guess = input("Guess: ")
        if is_p_int(guess):
            guess = int(guess)
            if guess > target:
                print("Too large!")
            elif guess < target:
                print("Too small!")
            else:
                print("Just right!")
                sys.exit()


def is_p_int(s):
    return s.isdigit() and int(s) > 0


main()
