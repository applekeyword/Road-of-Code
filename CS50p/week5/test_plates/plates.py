def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <= len(s) <= 6:
        return False
    if not s[:2].isalpha():
        return False

    for idx, ele in enumerate(s):
        if ele.isalpha():
            pass
        elif ele.isdigit():
            if ele == '0':
                return False
            else:
                return s[idx:].isdigit()
        else:
            return False
    return True


if __name__ == "__main__":
    main()
