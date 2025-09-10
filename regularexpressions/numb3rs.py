import re

def main():
    validate()

def validate():
    ip = input("IPv4 Address: ")
    if match := re.match(r"^([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])$", ip):
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    main()