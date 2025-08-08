import random
import string
#######################################################
def start_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance: $"))
            if balance <= 0:
                print("Balance must be a positive number.")
            else:
                print("\nWelcome to the Slot Machine Game!")
                print(f"You start with a balance of ${balance}")
                return balance
        except ValueError:
            print("Please enter a valid number.")
#######################################################
def bet_amount(balance):
    while True:
        try:
            bet_amount = int(input("Enter your bet amount: $"))
            if bet_amount <= 0 or bet_amount > balance:
                print(f"Invalid bet amount. You can bet between $1 and ${balance}")
            else:
                print(f"You bet ${bet_amount}")
                return bet_amount
        except ValueError:
            print("Please enter a valid number.")

#######################################################
def lottery():
    elements = list([1, 2, 3, 4, 5, 6])
    random_selection = random.choices(elements, k=3)
    return random_selection
#######################################################
def count(random_list):
    max_count = 0
    for i in range(len(random_list)):
        counter = 0
        temp = random_list[i]
        for j in range(len(random_list)):
            if temp == random_list[j]:
                counter += 1
        if counter > max_count:
            max_count = counter
    return max_count
#######################################################
def game(count_number, balance, bet_money):
    if count_number == 1:
        print("You lost")
        balance = balance - bet_money
        return balance
    elif count_number == 2:
        print("You won $", bet_money*2)
        balance = (bet_money*2) + (balance - bet_money)
        return balance
    else:
        print("You won $", bet_money*10)
        balance = (bet_money * 10) + (balance - bet_money)
        return balance

#######################################################
def question():
    while True:
        play_again = input("Do you want to play again? (y/n)").strip().lower()
        if play_again != "y" and play_again != "n":
             print("Print y or n , a valid input please")
            # continue
        elif play_again == "y":
            return True
        else:
            print("Thanks and Bye")
            return False

#######################################################

balance = start_balance()
print(f"\ncurrent balance: {balance}")

while True:
    bet_money = bet_amount(balance)
    print(bet_money)
    print("****************")
    print("Game result:")

    random_list = lottery()
    print(random_list)
    count_number = count(random_list)
    rest_balance = game(count_number, balance, bet_money)
    print(f"Current Balance: ${rest_balance}")

    if rest_balance > 0:
        if question():
            balance = rest_balance
            continue
        else:
            balance = rest_balance
            print(f"Current balance: {balance}")
            break
    else:
        balance = rest_balance
        print(f"Current balance: {balance}")
        print("Lost all credits!")
        break








