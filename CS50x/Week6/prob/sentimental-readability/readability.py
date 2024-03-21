from cs50 import get_string


def main():
    text = get_string("Text: ")

    index = clindex(text)
    if index >= 16:
        print("Grade 16+")
    elif index <= 0:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


def clindex(text):
    # calculate the cl-index
    letters_num = len([c for c in text if c.isalpha()])
    words_num = len(text.split())
    sentences_num = text.count(".") + text.count("!") + text.count("?")

    L = letters_num / words_num * 100
    S = sentences_num / words_num * 100
    index = round(0.0588 * L - 0.296 * S - 15.8)

    return index


if __name__ == "__main__":
    main()
