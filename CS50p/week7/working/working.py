import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r"([\d:]+) (AM|PM) to ([\d:]+) (AM|PM)", s):
        s = re.sub(r"([\d:]+) (AM|PM)", convert_12_to_24, s)
        return s
    else:
        raise ValueError


def convert_12_to_24(match):
    time = match.group(1).split(":")
    if match.group(2) == "PM" and int(time[0]) != 12:
        time[0] = int(time[0]) + 12
    elif match.group(2) == "AM" and int(time[0]) == 12:
        time[0] = 0
    if len(time) == 1:
        if 0 <= int(time[0]) <= 23:
            return f"{int(time[0]):02}:00"
        else:
            raise ValueError
    else:
        if 0 <= int(time[0]) <= 23 and 0 <= int(time[1]) <= 59:
            return f"{int(time[0]):02}:{int(time[1]):02}"
        else:
            raise ValueError


if __name__ == "__main__":
    main()
