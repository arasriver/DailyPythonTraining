import random


def user_input():
    user_in = input("Rock, Paper, Scissors? (r/p/s) ").lower().strip()
    return user_in


def computer_input():
    items = ['r', 'p', 's']
    computer = random.choice(items)
    return computer


def competition(user, computer):
    print(f"You chose {user}")
    print(f"Computer chose {computer}")
    if user == computer:
        print("equal")
    elif (user == "s" and computer == "p") or \
        (user == "p" and computer == "r") or \
        (user == "r" and computer == "s"):
        print("You won")
    else:
        print("Computer won")


while True:
    user = user_input()
    comp = computer_input()
    if user == 'r' or user == 'p' or user == 's':
        competition(user, comp)
        con = input("continue? (y/n): ").lower().strip()
        if con != "y":
            break
    else:
        print("Invalid choice")
        continue



# time_round = int(input("How many round do you want to play? "))
# for i in range(time_round):
#     user = user_input()
#     comp = computer_input()
#     if user == 'r' or user == 'p' or user == 's':
#         competition(user, comp)
#     else:
#         print("Invalid choice")
#         continue