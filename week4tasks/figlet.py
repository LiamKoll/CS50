import pyfiglet
import sys
import random
font = []
all_fonts = pyfiglet.FigletFont.getFonts()
font.extend(all_fonts)
def main():
    if len(sys.argv) == 1:
        qsecond = input("Input: ")
        ran = random.choice(font)
        result2 = pyfiglet.figlet_format(qsecond, font=ran)
        print(f"Output:\n{result2}")
    elif len(sys.argv) == 3 and ((sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font):
        qfirst = input("Input: ")
        result = pyfiglet.figlet_format(qfirst, font=sys.argv[2])
        print(f"Output:\n{result}")
    else:
        print("Invalid")
        sys.exit()

if __name__ == '__main__':
    main()