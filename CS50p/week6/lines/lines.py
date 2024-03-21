import sys


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        count = 0
        for row in file:
            if row.lstrip().startswith("#"):
                pass
            elif row.isspace():
                pass
            else:
                count += 1
        print(count)
except FileNotFoundError:
    sys.exit("File does not exist")
