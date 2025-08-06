import random


def create_number(length):
    while True:
        digits = random.sample(range(10), length)
        if digits[0] != 0:
            number = ''.join(map(str, digits))
            break

    return number


def has_unique_digits(number_str, length):
    return len(set(number_str)) == length


def comparison(guess, target_number, length):
    bulls = 0
    cows = 0
    for i in range(length):
        for j in range(length):
            if target_number[i] == guess[j]:
                if i == j:
                    bulls += 1
                else:
                    cows += 1

    print(f"{cows} Cows, {bulls} Bulls")


length = int(input("How many length should have the secret number? "))
target_number = create_number(length)
#print(target_number)
print(f"I have generated a {length}-digit number with unique digits. Try to guess it!")

while True:
    guess = input("Guess: ")
    if len(guess) != length or guess[0] == "0" or has_unique_digits(guess, length) is False:
        print("INVALID GUESS, Please enter a 4-digit number with unique digits")
        continue
    elif guess == target_number:
        print("SUCCESSFUL! YOU WON")
        break
    else:
        comparison(guess, target_number, length)
        continue
