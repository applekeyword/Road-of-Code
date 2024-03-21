menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

money = 0
try:
    while True:
        item = input("Item: ")
        p = menu.get(item.title())
        if p:
            money += p
            print(f"Total: ${money:.2f}")
except EOFError:
    pass

