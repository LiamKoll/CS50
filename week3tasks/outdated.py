def main():
    months =[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input("Date: ")
        try:
            m,d,y = date.split("/")
            newm = int(m)
            newd = int(d)
            newy = int(y)
            if (newm >= 1 and newm <= 12) and (newd >= 1 and newd <= 31):
                print(f"{newy}-{newm}-{newd}")
                break
        except:
            try:
                om, od, oy = date.split(" ")
                for month in months:
                    if om == months[month]:
                        m = month + 1
                d = od.replace(",", "")
                if (newm >= 1 and newm <= 12) and (newd >= 1 and newd <= 31):
                    print(f"{newy}-{newm}-{newd}")
                    break
            except:
                print("")
                pass

if __name__ == '__main__':
    main()