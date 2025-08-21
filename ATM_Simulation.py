###########################
def create_pin():
    while True:
        try:
            pin_code = int(input("Write the PIN code: "))
            return pin_code
        except ValueError:
            print("PIN code should be a number")

###########################
def check_pin(pin):
    while True:
        try:
            pin_code = int(input("Enter your PIN code: "))
            if pin_code == pin:
                return True
            else:
                print("Wrong pin code, try again")
                continue
        except ValueError:
            print("PIN code should be a number")

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
                keep_track.append(f"You deposited {depo_amount}")
                return current_balance
            else:
                raise ValueError
        except ValueError:
            print("Enter a valid amount!")
###########################
def withdraw(current_balance):
    while True:
        try:
            if current_balance == 0:
                print("Can not withdraw! No money in account")
                return current_balance
            withdraw_amount = int(input("Enter the amount to withdraw: "))
            if 0 < withdraw_amount <= current_balance != 0:
                current_balance = current_balance - withdraw_amount
                print(f"Successfully withdrew ${withdraw_amount} \n")
                keep_track.append(f"You withdrew {withdraw_amount}")
                return current_balance
            else:
                print(f"Current credit is {current_balance}")
                print(f"Withdraw amount should be between 0  and {current_balance} \n")
                continue
        except ValueError:
            print("Enter a valid amount!!")

###########################
amount = 0
current_balance = 0
keep_track = []

pin = create_pin()
pin_check = check_pin(pin)

if pin_check is True:
    while True:
        print("Welcome to ATM")
        print(" 1. Check Balance\n 2. Deposit \n 3. Withdraw \n 4. Exit \n 5. Track transactions")
        try:
            option = int(input("Please choose an option: "))
            if option != 1 and option != 2 and option != 3 and option !=4 and option !=5:
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
                amount = withdraw(amount)
            elif option == 5:
                for i in range(len(keep_track)):
                    print(keep_track[i])
                print("\n")
        except ValueError:
            print("Enter a valid number \n")


