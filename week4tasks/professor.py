import random as r

def main():
    level = get_level()
    score = game(level)
    print(f"Score = {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            while level == 1 or level == 2 or level == 3:
                return level
                break
        except:
            pass

def generate_integer(level):
    if level == 1 or level == 2 or level == 3:
        x = r.randint(0,9)
        y = r.randint(0,9)
        return x,y

def round(x, y):
    tries = 1
    while tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                print("EEE")
                tries += 1
        except:
            print("EEE")
            tries += 1
    print(f"{x} + {y} = {x+y}")
    return False

def game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = round(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score


if __name__ == "__main__":
    main()