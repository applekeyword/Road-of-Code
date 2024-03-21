l = input("Expression: ").split()

match l[1]:
    case "+":
        print(f"{int(l[0]) + int(l[2]):.1f}")
    case "-":
        print(f"{int(l[0]) - int(l[2]):.1f}")
    case "*":
        print(f"{int(l[0]) * int(l[2]):.1f}")
    case _:
        print(f"{int(l[0]) / int(l[2]):.1f}")
