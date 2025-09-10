from twttr import vowels

def main():
    q = str(input("Input: \n")).capitalize()
    shorten(q)


def shorten(word):
    vowels(word)


if __name__ == "__main__":
    main()