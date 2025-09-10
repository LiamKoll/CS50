import re
import sys
import tabulate
import csv

def main():
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) == 2:
        r = re.match(r"^.*\.csv$", sys.argv[1])
        if r:
            try:
                with open(rf"{sys.argv[1]}", "r") as f:
                    c = csv.reader(f)
                    print(tabulate.tabulate(c, tablefmt="grid"))
            except:
                print("File does not exist")
                sys.exit()
        else:
            print("Not a CSV file")
            sys.exit()


if __name__ == '__main__':
    main()