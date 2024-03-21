from cs50 import get_int


def main():
    while True:
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break

    for i in range(height):
        print_row(height, i)


def print_row(height, row):
    for i in range(height - row - 1):
        print(" ", end="")
    for i in range(row + 1):
        print("#", end="")
    print("  ", end="")
    for i in range(row + 1):
        print("#", end="")
    print()


if __name__ == "__main__":
    main()
