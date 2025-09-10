def main():
    coke()

def coke():
    amountdue = 50
    while amountdue > 0:
        print(f"Amount Due: {amountdue}")
        a = int(input("Insert Coin: "))
        coins = [5, 10, 25]
        if a in coins:
            amountdue -= a

    if amountdue <= 0:
        print(f"Change Owed: {-amountdue}") # abs() can be also implemented instead of -


if __name__ == '__main__':
    main()