import inflect
import sys

p = inflect.engine()
names = []
try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    pass

print("Adieu, adieu, to", p.join(names))
