import sys
import re

def main():
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit()
        elif len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit()
        elif len(sys.argv) == 2:
            r = re.match(r"^.*\.py$", sys.argv[1])
            if r:
                try:
                    with open(rf"{sys.argv[1]}", "r") as f:
                        x = len(f.readlines())
                        print(x)
                except:
                    print("File does not exist")
                    sys.exit()
            else:
                print("Not a Python file")
                sys.exit()



if __name__ == '__main__':
    main()