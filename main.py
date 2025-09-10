'''# sudo-language -> structure + ideas, sort program

# Name variable + entfernt whitespace + Großschrebung
name = input("Whats your name? ").strip().title()

# Abfrage
print(f"Hello, {name}", sep=" ",end="!") # f = besondere quote/str, sep für separate und end = ende des strings, \n = neue Zeile
'''

'''x = float(input("Was ist x?"))
y = float(input("Was ist y?"))

z = round(x + y,2)

print(f"{z:,}")'''
'''
def hello(to):
    print("Hallo,", to, end="!")

name = input("Wat is dein name? ")
hello(name) '''

'''
x = int(input("Wat ist deine nummer für x?"))
y = int(input("Wat ist deine nummer für y?"))

if x < y:
    print("y ist größer")
elif x == y:
    print("x ist gleich y")
else:
    print("x ist größer")
'''
'''
x = int(input("Wat ist deine nummer für x?"))
y = int(input("Wat ist deine nummer für y?"))

if x == y:
    print("x ist gleich y!")
else:
    print("x ist nicht gleich y!") '''
'''
score = int(input("Score:"))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Grade F")
'''

'''
def main():
    x = int(input("Ist die Nummer Even oder Odd? "))
    if iseven(x) == True:
        print("Die Nummer ist Even!")
    else:
        print("Die Nummer ist Odd!")

def iseven(n):
    return n % 2 == 0
main()
'''
'''
#house + match

name = input("Wie heißt du? ")
match name:
    case "Liam" | "King" | "Boss":
        print("Schöner Name!")
    case _:
        print("Hässliche Namen")
'''
'''
for _ in range(0,3):
    print("Meow")
'''
'''
def main():
    num = get_num()
    meow(num)

def get_num():
    while True:
       n = int(input("Welche nummer?"))
       if n > 0:
        return n
        
def meow(n):
    for _ in range(n):
        print("meow")

main()
'''
'''
students = ["Liam", "Boss", "King"]

for i in range(len(students)):
    print(i +1,students[i]) '''
'''
students = {
    "Liam": "Villa",
    "Boss": "Villa",
    "King": "Burg"
}

for student in students:
    print(student, students[student], sep=", ")

students = [
    {"name":"Liam", "Ziel":"improvement", "Essen":"Döner"},
    {"name":"Marvin", "Ziel":"Wixxen", "Essen":"Mcces"},
    {"name":"Dennis", "Ziel":"Picasso", "Essen":"Hähnchen"}
]

for student in students:
    print(student["name"], student["Ziel"], sep=", ")
'''
'''
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)
main()
'''
'''
def main():
    x = get_int()
    print(f"x ist {x}!")

def get_int():
    while True:
        try:
            x = int(input("Was ist x?"))
        except ValueError:
            print("X ist keine Nummer!")
        else:
            return x
'''
'''
import random
cards =["Fortnite","Minecraft","CSGO"]
random.shuffle(cards)
for card in cards:
    print(card)
'''
'''
import statistics
grades = [100, 90]
print(statistics.mean(grades))
'''
'''
import sys
# check für fehler
if len(sys.argv) < 2:
    sys.exit("Zu wenig")

for arg in sys.argv[1:]:
    print(arg)
'''
'''
import requests
import json
name = input("Gib den Namen des Künstlers ein!")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + name)

o = response.json()

for result in o["results"]:
    print(result["trackName"])
'''
