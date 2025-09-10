def main():
    file()

def file():
    q = input("File name:\n").strip()
    suffix = [".gif",
            ".jpg",
            ".jpeg",
            ".png",
            ".pdf",
            ".txt",
            ".zip"]

    if suffix[0] in q:
        print("Image/gif")
    elif suffix[1] in q or suffix[2] in q:
        print("Image/jpeg")
    elif suffix[3] in q:
        print("Image/png")
    elif suffix[4] in q:
        print("application/pdf")
    elif suffix[5] in q:
        print("text/plain")
    elif suffix[6] in q:
        print("application/zip")
    else:
        print("application/octet-s")

if __name__ == '__main__':
    main()