import random


def main():
    level = get_level()

    scores = [0 for _ in range(10)]
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for _ in range(3):
            answer = input(f"{x} + {y} = ")
            if answer.isdigit() and x + y == int(answer):
                scores[i] = 1
                break
            else:
                print("EEE")
        if not scores[i]:
            print(f"{x} + {y} = {x + y}")
    print("Score:", sum(scores))


def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level in [2, 3]:
        return random.randint(10 ** (level - 1), 10 ** level - 1)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
