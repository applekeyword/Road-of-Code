def main():
    text = input("Input: ")
    text = shorten(text)
    print(f"Output: {text}")


def shorten(word):
    for s in word:
        if s.lower() in ["a", "e", "i", "o", "u"]:
            word = word.replace(s, "")
    return word


if __name__ == "__main__":
    main()
