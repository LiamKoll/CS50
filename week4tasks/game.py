import random
import sys


def main():
    level()

def level():
    while True:
        try:
            level = int(input("Level: "))
            ran = random.randint(1, level)
            while level >= 1:
                try:
                    guess = int(input("Guess: "))
                    if guess >= 1:
                        if guess > ran:
                            print("Too large!")
                            pass
                        elif guess < ran:
                            print("Too small!")
                            pass
                        elif guess == ran:
                            print("Just right!")
                            sys.exit()
                        else:
                            pass
                except ValueError:
                    pass
        except ValueError:
            pass




if __name__ == '__main__':
    main()
    
# That was enjoyment!!!! 01.05.2024 Liam