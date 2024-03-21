import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    for row in reader:
        if row["state"] in new_cases:
            new_cases[row["state"]].append(int(row["cases"]))
            if len(new_cases[row["state"]]) > 14:
                new_cases[row["state"]].pop(0)
        else:
            new_cases[row["state"]] = []
            new_cases[row["state"]].append(int(row["cases"]))

    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    records = {}
    for state in states:
        records[state] = {}
        # rounding??????
        before_avg = sum(new_cases[state][0:7]) / 7
        cur_avg = sum(new_cases[state][7:]) / 7
        records[state]["cases"] = cur_avg
        try:
            percent = abs((before_avg - cur_avg) / before_avg)
        except ZeroDivisionError:
            percent = 0

        records[state]["percent"] = percent
        if before_avg > cur_avg:
            records[state]["status"] = "decrease"
        elif before_avg < cur_avg:
            records[state]["status"] = "increase"
        else:
            records[state]["status"] = "no change"

    for state, data in records.items():
        if data["status"] != "no change":
            print(f"{state} had a 7-day average of {data['cases']} and a {data['status']} of {data["percent"]}.")
        else:
            print(f"{state} had a 7-day average of {data['cases']} and {data['status']}.")


if __name__ == "__main__":
    main()
