def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    l = fraction.split("/")
    fuel = int(l[0]) / int(l[1])
    if fuel > 1:
        raise ValueError
    else:
        return round(fuel * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
