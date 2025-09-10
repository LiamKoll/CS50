def main():
    character = get_character()
    if character[0] == "Anakin":
        character[1] = "Tatooine"
    print(f"{character[0]} is from {character[1]}")

def get_character():
    name = input("Name:\n")
    planet = input("Planet: \n")
    return (name, planet)

if __name__ == '__main__':
    main()