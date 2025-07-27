import random

times = int(input("How many dice do you want to roll? "))
dice = input("Roll the dice? (y/n): ").lower()
counter = 0
while dice != "n":
    if dice == "y":
        for i in range(times):
            result = (random.randint(1,6),random.randint(1,6))
            counter += 1
            print(result)
    else:
        print("Invalid choice! ")

    dice = input('Roll the dice? (y/n): ').lower()

print("Thanks for playing")
print(f"number of dice rolling: {counter}")

