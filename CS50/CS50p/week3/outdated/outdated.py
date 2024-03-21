months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    text = input("Date: ").strip()
    if text[0].isdigit():
        l = text.split("/")
        if len(l) == 3 and int(l[0]) <= 12 and int(l[1]) <= 31:
            print(f"{l[2]}-{int(l[0]):02}-{int(l[1]):02}")
            break
    else:
        l = text.split()
        try:
            idx = months.index(l[0])
        except ValueError:
            pass
        if len(l) == 3 and l[1][-1] == "," and int(l[1].rstrip(",")) <= 31:
            print(f"{l[2]}-{idx + 1:02}-{int(l[1].rstrip(",")):02}")
            break

