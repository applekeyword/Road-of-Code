import inflect
import sys

from datetime import date

def main():
    time_string = input("Date of Birth: ")
    try:
        days = get_delta_days(time_string)
    except:
        sys.exit("Invalid date")

    p = inflect.engine()
    print(p.number_to_words(days * 24 * 60, andword="").capitalize(), "minutes")

def get_delta_days(time_string):
    delta = date.today() - date.fromisoformat(time_string)
    return delta.days

if __name__ == "__main__":
    main()
