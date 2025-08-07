import random
import string

password_numbers = 0
password_length = 0
password_list = []
while True:
    try:
        password_length = int(input("Enter password length: "))
        password_numbers = int(input("How many passwords do you need? "))
        if password_length and password_numbers > 0:
            lowercase = ''.join(random.choices(string.ascii_lowercase, k=password_length))
            password_list.append(lowercase)
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid Input")
        continue


while True:
    include_upper = input("Include uppercase letters? (y/n) ").lower().strip()
    if include_upper == "y":
        uppercase = ''.join(random.choices(string.ascii_uppercase, k=password_length))
        password_list.append(uppercase)
        break
    elif include_upper == "n":
        break
    else:
        print("Enter a valid character, y or n!")
        continue

while True:
    include_numbers = input("Include numbers? (y/n) ").lower().strip()
    if include_numbers == "y":
        digits = ''.join(random.choices(string.digits, k=password_length))
        password_list.append(digits)
        break
    elif include_numbers == "n":
        break
    else:
        print("Enter a valid character, y or n!")
        continue

while True:
    include_special = input("Include Special Characters? (y/n) ").lower().strip()
    if include_special == "y":
        special_char = "&^*$%%@#@"
        special_characters = ''.join(random.choices(special_char, k=password_length))
        password_list.append(special_characters)
        break
    elif include_special == "n":
        break
    else:
        print("Enter a valid character, y or n!")
        continue


temporary_list = []

while password_numbers > 0:
    password_numbers -= 1
    for i in range(100):
        for j in password_list:
            a = ''.join(random.choices(j, k=1))
            temporary_list.append(a)
    final_password = ''.join(random.choices(temporary_list, k=password_length))
    print(final_password)
    with open("passwords.txt", "a") as f:
        f.write(final_password + "\n")

