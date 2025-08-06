import re

password = input("Enter a password: ")
length = 8
check_digit = re.findall("[0-9]", password)
check_special = re.findall("\W", password)
check_lower = re.findall("[a-z]", password)
check_upper = re.findall("[A-Z]", password)

if len(password) < length:
    print("Very Weak")
elif check_digit and check_lower and check_upper and check_special:
    print("Very Strong")
elif check_digit and check_lower and check_upper:
    print("Strong")
elif check_digit and (check_lower or check_upper):
    print("Medium")
else:
    print("Weak")




