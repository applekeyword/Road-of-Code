def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    text = input("Input a sentence: ")
    text = convert(text)
    print(text)


main()
