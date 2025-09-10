import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    form = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if form:
        pieces = form.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        first_time = ger_format(pieces[1], pieces[2], pieces[3])
        second_time = ger_format(pieces[5], pieces[6], pieces[7])
        return first_time + " to " + second_time
    else:
        raise ValueError

def ger_format(h, m, am_pm):
    if am_pm == "PM":
        if int(h) == 12:
            new_h = 12
        else:
            new_h = int(h) + 12
    else:
        if int(h) == 12:
            new_h = 0
        else:
            new_h = int(h)
    if m == None:
        new_m = ":00"
        new_time = f"{new_h:02}" + new_m
    else:
        new_time = f"{new_h:02}" + ":" + m
    return new_time









if __name__ == "__main__":
    main()