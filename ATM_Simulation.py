###########################
def balance(amount):
    return amount
###########################
def deposit(current_balance):
    while True:
        try:
            depo_amount = int(input("Enter the amount to deposit: "))
            if depo_amount > 0:
                current_balance = depo_amount + current_balance
                print(f"Successfully deposited ${depo_amount} \n")
                return current_balance
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid amount!")
###########################
def withdraw(current_balance):
    while True:
        try:
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            if 0 < withdraw_amount <= current_balance:
                current_balance = current_balance - withdraw_amount
                print(f"Successfully withdrew ${withdraw_amount} \n")
                return current_balance
            else:
                print(f"Current credit is {current_balance}")
                print(f"Withdraw amount should be between 0  and {current_balance} \n")
                continue
        except ValueError:
            print("Enter a valid amount!")

###########################
amount = 0
current_balance = 0
while True:
    print("Welcome to ATM")
    print(" 1. Check Balance\n 2. Deposit \n 3. Withdraw \n 4. Exit")
    try:
        option = int(input("Please choose an option: "))
        if option != 1 and option != 2 and option != 3 and option !=4:
            print("Enter a valid number for option between 1 to 4 \n")
            continue
        if option == 4:
            print("Good Bye")
            break
        elif option == 1:
            current_balance = balance(amount)
            print(f"Your current balance is: {current_balance} \n")
        elif option == 2:
            amount = deposit(current_balance)
        elif option == 3:
            amount = withdraw(current_balance)
    except ValueError:
        print("Enter a valid number \n")


