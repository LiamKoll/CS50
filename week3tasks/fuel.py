def main():
    while True:
        q = input("Fraction: ")
        try:
            x,y = q.split("/")
            new_x = int(x)
            new_y = int(y)
            calc = new_x / new_y
            if calc <= 1:
                break
        except (ValueError, ZeroDivisionError):
            pass
    p = int(calc * 100)
    if p <= 1:
        print("E")
    elif p >= 99:
        print("F")
    else:
        print(f"{p}%")

"""def fuel(s):
    x,j,y = s.split(" ")
    new_x = int(x)
    new_y = int(y)
    try:

        if new_x > new_y:
            raise ValueError
        elif new_y == 0:
           raise ZeroDivisionError
        elif j == "/":
            print(new_x / new_y)
        else:
            raise ValueError

    except (ValueError, ZeroDivisionError):
        main()"""



if __name__ == '__main__':
    main()