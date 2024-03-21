from cs50 import get_float


def main():
    cents = get_input()
    num_coins = min_coins(cents)

    print(num_coins)


def get_input():
    while True:
        money = get_float("Change owed: ")
        if money > 0:
            return money * 100


def min_coins(money):
    coins = {}
    coins["quarters"] = money // 25
    money -= 25 * coins["quarters"]
    coins["dimes"] = money // 10
    money -= 10 * coins["dimes"]
    coins["nickels"] = money // 5
    money -= 5 * coins["nickels"]
    coins["pennies"] = money

    return int(coins["quarters"] + coins["dimes"] + coins["nickels"] + coins["pennies"])


if __name__ == "__main__":
    main()
