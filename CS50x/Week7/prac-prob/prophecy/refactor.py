import csv
import sqlite3

conn = sqlite3.connect('refactor.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE students (
    id INTEGER,
    name TEXT,
    PRIMARY KEY(id)
    )
''')
cursor.execute('''
    CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
    )
''')
cursor.execute('''
    CREATE TABLE house_assignments (
    student_id INTEGER,
    house_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(house_id) REFERENCES houses(id)
    )
''')

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("INSERT INTO students (name) VALUES (?)", (row["student_name"],))
        student_id = cursor.lastrowid
        cursor.execute("INSERT INTO houses (house, head) VALUES (?, ?)", (row["house"], row["head"]))
        house_id = cursor.lastrowid
        cursor.execute("INSERT INTO house_assignments (student_id, house_id) VALUES (?, ?)", (student_id, house_id))

conn.commit()
conn.close()