from cs50 import get_string
import sys


def main():
    number = get_string("Number: ")

    if not luhn_valid(number):
        print("INVALID")
        sys.exit(0)

    status = struct_valid(number)
    print(status)


def struct_valid(number):
    first = int(number[0])
    first_two = int(number[0:2])
    length = len(number)

    if first == 4 and (length == 13 or length == 16):
        return "VISA"
    elif first_two in range(51, 56) and length == 16:
        return "MASTERCARD"
    elif (first_two == 34 or first_two == 37) and length == 15:
        return "AMEX"
    else:
        return "INVALID"


def luhn_valid(number):
    num_list = [int(digit) for digit in number]
    to_prod_list = num_list[-2::-2]
    rem_lsit = num_list[-1::-2]

    splited_list = []
    for num in to_prod_list:
        num *= 2
        if num >= 10:
            tmp = [int(digit) for digit in str(num)]
            splited_list += tmp
        else:
            splited_list.append(num)

    status = (sum(rem_lsit) + sum(splited_list)) % 10
    if status == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
