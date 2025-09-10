import emoji
def main():
    ask()

def ask():
    q = input("Input: ")
    print(emoji.emojize(f"Output: {q}", language='alias'))

if __name__ == '__main__':
    main()