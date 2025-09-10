import sys
import csv
import re

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) == 3:
            try:
                with open(rf"{sys.argv[1]}", "r") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        last, first = row["name"].rstrip().split(",")
                        house = row["house"].rstrip()
                        print(f"{first} {last} lives in {house}")
                        try:
                            r = re.match(r"^.*\.csv$", sys.argv[2])
                            if r:
                                with open(f"{sys.argv[2]}", "a") as file:
                                    file.write(f"{first}, {last}, {house}\n")
                        except:
                            sys.exit()

            except:
                print(f"Could not read {sys.argv[1]}")
                sys.exit()

if __name__ == '__main__':
    main()