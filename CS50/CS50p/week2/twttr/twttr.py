text = input("Input: ")

for s in text:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        text = text.replace(s, "")

print(f"Output: {text}")
