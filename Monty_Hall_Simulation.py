import random

def monty_hall_interactive():
    doors = [0, 0, 1]  # 0 = goat, 1 = car
    random.shuffle(doors)  # Shuffle doors randomly

    # User picks a door
    while True:
        try:
            choice = int(input("Choose a door (1, 2, or 3): ")) - 1  # Convert to 0-based index
            if choice not in [0, 1, 2]:
                print("Please choose 1, 2, or 3!")
                continue
            break
        except ValueError:
            print("Enter a valid number!")

    # Monty opens a door with a goat
    possible_doors = [i for i in [0, 1, 2] if i != choice and doors[i] == 0]
    monty_opens = random.choice(possible_doors)  # Monty picks a door with a goat

    print(f"Monty opens door {monty_opens + 1}, which has a goat.")

    # User decides to switch or not
    while True:
        switch = input("Do you want to switch doors? (yes/no): ").strip().lower()
        if switch in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'!")

    # If user wants to switch
    if switch == "yes":
        choice = 3 - choice - monty_opens  # Switch to the remaining door

    # Result
    if doors[choice] == 1:
        print(f"You chose door {choice + 1} and won the car!")
    else:
        print(f"You chose door {choice + 1} and got a goat!")

# Run the game
print("Welcome to the Monty Hall game!")
monty_hall_interactive()