import re

def main():
    q = str(input("Input: \n")).capitalize()
    vowels(q)

def vowels(input):
    output = re.sub(r"[AEIOU]", "",input , flags=re.IGNORECASE)
    print(f"Output: {output}")

if __name__ == '__main__':
    main()