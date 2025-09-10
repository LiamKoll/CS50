import inflect as inf
names = []
on = inf.engine()
def main():
    adieu()

def adieu():
    while True:
        try:
            q = input("Name: ")
            names.append(q)         # append() inserts input into list
        except EOFError:
            print("")
            break
    output = on.join(names)
    print(f"Adieu, adieu, to {output}")


if __name__ == '__main__':
    main()