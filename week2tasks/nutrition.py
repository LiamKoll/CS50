def main():
    q = input("Item: ").lower()
    calories(q)

def calories(s):
    fc = [
        {"fruit":"banana", "calorie": "110"},
        {"fruit":"apple", "calorie": "130"},
        {"fruit":"avocado", "calorie": "50"}
        ]
    for fruitcal in fc:
        if s in fruitcal["fruit"]:
            print(f"Calories: {fruitcal['calorie']}")

if __name__ == '__main__':
    main()