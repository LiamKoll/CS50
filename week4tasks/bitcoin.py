import requests
import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit()
    try:
        m = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit()

    amount = m * calc()
    r = round(amount,4)
    f = ('{:,}'.format(r))
    print(f"${f}")
def calc():
    try:
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = res.json()
        return o["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        print("RequestException")
        sys.exit()


if __name__ == '__main__':
    main()