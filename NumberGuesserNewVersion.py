import random

print("***Welcome to number guesser game!***")
print("To exit the game enter -1")
print("Determine range of interval")
low = int(input("lower number: "))
high = int(input("higher number: "))
opportunity = int(input("How many times do you want to guess? max: "))

while high < low:
    print("higher number can not be lower that lower number!!!!")
    print("Let's try again")
    low = int(input("lower number: "))
    high = int(input("higher number: "))

true_number = random.randint(low,high)
step = 0

while step != opportunity:
    try:
        guessed_number = int(input(f"Guess a number between {low} and {high}: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue

    if guessed_number == -1:
        print("Exiting game. Thanks for playing!")
        break

    if guessed_number < 0 or guessed_number > 100:
        print("Invalid number")
        continue

    if guessed_number == true_number:
        print(f"You won after {step} steps")
        step += 1
        break
    else:
        if guessed_number > true_number:
            print("too high!!", "Try a number less than ", guessed_number)
            step += 1
        else:
            print("too low!!", "Try a number greater than ", guessed_number)
            step += 1
print(f"you have tried {opportunity} times. OUT OF LIMITATION!")

print(f"True number is {true_number}")