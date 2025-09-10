def main():
    greeting()

def greeting():
    g = input("Greeting: ")

    if "Hello" in g:
        print("$0")

    elif "H" in g:
        print("$20")

    else:
        print("$100")

if __name__ == '__main__':
    main()
