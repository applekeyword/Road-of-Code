answer = input("What is the answer to Great Question of Life, the Universe, and Everything? ")

if answer.strip().lower() in ["42", "forty-two", "forty two"]:
    print("Yes")
else:
    print("No")
