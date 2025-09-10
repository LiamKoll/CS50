import csv

name = input("Wie heißt du? \n")
wohnort = input("Wo wohnst du? \n")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "wohnort"])
    writer.writerow({"name":name, "wohnort":wohnort})
