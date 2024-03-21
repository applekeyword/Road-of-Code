import json
import sys
import requests


if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# get the requested json
# print(json.dumps(r.json(), indent=2))

money = r.json()["bpi"]["USD"]["rate_float"] * amount
print(f"${money:,.4f}")
