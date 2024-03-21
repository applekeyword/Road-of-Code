items = {}
try:
    while True:
        item = input().upper()
        items[item] = items.get(item, 0) + 1
except EOFError:
    for key, value in sorted(items.items()):
        print(value, key)
