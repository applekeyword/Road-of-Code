def main():
    fuel = get_fuel("Fraction: ")
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")


def get_fuel(prompt):
    while True:
        l = input(prompt).split("/")
        try:
            fuel = int(l[0]) / int(l[1])
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if fuel <= 1:
                return round(fuel * 100)


if __name__ == "__main__":
    main()
