def main():
    calc()

def calc():
    q = input(f"Expression: ")
    x, y, z = q.split(" ")
    new_x = float(x)
    new_z = float(z)

    if y == "+":
        print(new_x + new_z)
    elif y == "-":
        print(new_x - new_z)
    elif y == "/":
        new_z != 0
        print(new_x / new_z)
    elif y == "*":
        print(new_x * new_z)

if __name__ == '__main__':
    main()