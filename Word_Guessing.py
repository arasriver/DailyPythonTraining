import random
import string
with open("Word_Guessing.txt") as f:
    words = f.read().splitlines()

target_word = random.choice(words)
target_word = target_word.lower()
length = len(target_word)
place_holder = "-" * length
print(place_holder)
print(target_word)
print("***************")

while True:
    letter = input("Enter a letter: ").lower().strip()
    if len(letter) != 1:
        print("Print just one letter, not more!")
        continue
    elif not letter.isalpha():
        print("Just a LETTER is possible ")
        continue
    elif letter in place_holder:
        print("You already guessed it")
        continue

    if letter not in target_word:
        print("Wrong Guess")
        continue
    else:
        print("Good Guess")
        new_placeholder = ""
        for i in range(len(target_word)):
            if target_word[i] == letter:
                new_placeholder += letter
            else:
                new_placeholder += place_holder[i]
        place_holder = new_placeholder

    print(place_holder)

    if place_holder == target_word:
        print("You guessed the word!")
        break




