def main():
    q = input("camelCase: ")
    format(q)

# s comprises each letter from the written word in q
def format(f):
    for s in f:
        # isupper() function looks out for Uppercase
        if s.isupper():
            # prints _ and the letter in the same line
            print("_" + s, end="")
        else:
            # resume with the other letters
            print(s, end="")


if __name__ == '__main__':
    main()