import random

dice = input("Roll the dice? (y/n): ").lower()
while dice != "n":
    if dice == "y":
        result = (random.randint(1,6),random.randint(1,6))
        print(result)
    else:
        print("Invalid choice! ")

    dice = input('Roll the dice? (y/n): ').lower()

print("Thanks for playing")

