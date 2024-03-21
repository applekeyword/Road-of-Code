name = input("camelCase: ")

for s in name:
    if s.isupper():
        name = name.replace(s, f"_{s.lower()}")

print(f"snake_case: {name}")
