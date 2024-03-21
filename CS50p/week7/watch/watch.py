import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # matches = re.search(r"src=\"https?://www.youtube.com/embed/", s)
    # if matches:
    if matches := re.search(r"src=\"https?://(?:www\.)?youtube.com/embed/(\w+)", s):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
