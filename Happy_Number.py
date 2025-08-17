
print("***Welcome to happy number*** ")

while True:
    try:
        number = int(input("Enter your number: "))
        if number > 0:
            break
        else:
            print("Enter a positive number")
            continue
    except ValueError:
        print("Enter a valid number\n")

seen_numbers = []
while (number != 1) and (number not in seen_numbers):
    seen_numbers.append(number)
    number = sum(int(i) ** 2 for i in str(number))

if number == 1:
    print("This is a happy number")
else:
    print("This is not a happy number")

