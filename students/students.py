import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "wohnort": row["wohnort"], "haus": row["haus"]})


for student in sorted(students, key=lambda student: student["name"]):        #creating a anonymous function
    print(f"{student['name']} wohnt in {student['wohnort']} in einer/m {student['haus']}")