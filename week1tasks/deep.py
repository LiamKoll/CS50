def main():
    question_to_life()

def question_to_life():
    q = input("What is the Answer to the Great Question of Life, the Universe, and Everything?\n")
    if q == "42" or q == "forty-two" or q == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()