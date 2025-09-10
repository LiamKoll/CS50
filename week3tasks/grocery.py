def main():
    grocerylist = {}
    while True:
        try:
            item = input("Item: ").upper()
            if item in grocerylist:
                grocerylist[item] += 1
            else:
                grocerylist[item] = 1

        except (EOFError):
            for piece in sorted(grocerylist):
                print(grocerylist[piece], piece, sep=" ")
            break

if __name__ == '__main__':
    main()