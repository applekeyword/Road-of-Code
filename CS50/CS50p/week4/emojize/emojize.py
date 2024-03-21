import emoji

text = input("Input: ")

if "_" in text:
    print(emoji.emojize(text))
else:
    print(emoji.emojize(text, language="alias"))
