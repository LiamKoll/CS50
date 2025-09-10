import sys
import re
from PIL import Image

def main():
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit()
    elif len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) == 3:
        jpg1 = re.match(r"^.*\.jpg$", sys.argv[1])
        jpg2 = re.match(r"^.*\.jpg$", sys.argv[2])
        jpeg1 = re.match(r"^.*\.jpeg$", sys.argv[1])
        jpeg2 = re.match(r"^.*\.jpeg$", sys.argv[2])
        png1 = re.match(r"^.*\.png$", sys.argv[1])
        png2 = re.match(r"^.*\.png$", sys.argv[2])
        if jpg1 or jpeg1 or png1:
            if jpg2 or jpeg2 or png2:
                if jpg1 and jpg2 or jpeg1 and jpeg2 or png1 and png2:
                    bild = Image.open(fr"{sys.argv[1]}")
                    shirt = Image.open(r"shirt.png")
                    size = shirt.size
                    resize = bild.resize(size)
                    resize.paste(shirt, shirt)
                    resize.save(f"{sys.argv[2]}")
                    print("Worked!")
                else:
                    print("Input and output have different extensions")
                    sys.exit()
            else:
                print("Invalid Output")
                sys.exit()

        else:
            print("Input does not exist")
            sys.exit()


if __name__ == '__main__':
    main()