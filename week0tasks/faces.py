def main():
    convert()

def convert():
    emoji = str(input())
    if ":)" in emoji or ":(" in emoji:
        print(emoji.replace(":)", "🙂").replace(":(", "🙁"))
    else:
        print(emoji)


if __name__ == '__main__':
    main()