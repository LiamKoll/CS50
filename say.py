from sayings import hello, goodbye

name = input("Was ist das Passwort?")

if name == "Liam":
    hello(name)

else:
    print("Leider Falsch!")
    goodbye(name)