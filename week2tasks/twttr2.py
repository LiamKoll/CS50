def main():
    q = input("Input: ").capitalize()
    removevowels(q)

def removevowels(s):
        newstr = s
        vowels = ["a", "e", "i", "o", "u"]
        for x in s.lower():
            if x in vowels:
                newstr = newstr.replace(x,"")

        print(f"Output: {newstr}")

if __name__ == '__main__':
    main()