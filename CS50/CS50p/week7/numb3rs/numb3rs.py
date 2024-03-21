import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    digits = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if digits:
        for i in range(1, 5):
            if not 0 <= int(digits.group(i)) <=255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
