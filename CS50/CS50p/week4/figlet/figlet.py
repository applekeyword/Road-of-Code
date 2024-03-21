from pyfiglet import Figlet
import random
import sys

argc = len(sys.argv)
fonts = Figlet().getFonts()

if argc == 1:
    font = random.choice(fonts)
elif argc == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

text = input("Input: ")
f = Figlet(font=font)
print(f.renderText(text))
