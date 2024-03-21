due = 50
print(f"Amount Due: {due}")

while due > 0:
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        due -= coin

    if due > 0:
        print(f"Amount Due: {due}")
    else:
        print(f"Change Owed: {-1 * due}")
