import random
def user_input():
    user = input("Rock, Paper, Scissors? (r/p/s) ").lower().strip()
    return user
def computer_input():
    items = ['r', 'p', 's']
    computer = random.choice(items)
    return computer
def competition(user, computer):
    print(f"You chose {user}")
    print(f"Computer chose {computer}")
    if user == computer:
        print("equal")
    elif user == "s" and computer == "p":
        print("You won")
    elif user == "p" and computer == "r":
        print("You won")
    elif user == "r" and computer == "s":
        print("You won")
    else:
        print("Computer won")


while True:
    user = user_input()
    comp = computer_input()
    if user == 'r' or user == 'p' or user == 's':
        competition(user, comp)
        con = input("continue? (y/n): ").lower().strip()
        if con == "y":
            continue
        else:
            break
    else:
        print("Invalid choice")
        continue








