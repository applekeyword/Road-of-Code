import sys
from PIL import Image
from PIL import ImageOps


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
    sys.exit("Input and output have different extensions")
if not sys.argv[1].split(".")[-1].lower() in ["jpg", "jpeg", "png"] or not sys.argv[2].split(".")[-1].lower() in ["jpg", "jpeg", "png"]:
    sys.exit("Invalid output")

try:
    img = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

shirt = Image.open("shirt.png")
img = ImageOps.fit(img, shirt.size)
img.paste(shirt, shirt)
img.save(sys.argv[2])
