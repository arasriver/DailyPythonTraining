import numpy as np

table = np.ones((3, 3), dtype=object)

while True:
    print(f"player no turn: ")
    while True:
        print(f"player X's turn: ")
        starter_row = int(input("Select a row 0,1 or 2 : "))
        if starter_row == 0 or starter_row == 1 or starter_row == 2:
            break
        else:
            print("Invalid input")
            continue

    while True:
        starter_col = int(input("Select a column 0,1 or 2 : "))
        if starter_col == 0 or starter_col == 1 or starter_col == 2:
            break
        else:
            print("Invalid input")
            continue

    table[starter_row][starter_col] = "X"

    print(f"player Y's turn: ")
    while True:
        starter_row = int(input("Select a row 0,1 or 2 : "))
        if starter_row == 0 or starter_row == 1 or starter_row == 2:
            break
        else:
            print("Invalid input")
            continue

    while True:
        starter_col = int(input("Select a column 0,1 or 2 : "))
        if starter_col == 0 or starter_col == 1 or starter_col == 2:
            break
        else:
            print("Invalid input")
            continue

    table[starter_row][starter_col] = 0

    if table[0][0] == "X" and table[0][1] == "X" and table[0][2] == "X" or \
            table[1][0] == "X" and table[1][1] == "X" and table[1][2] == "X" or \
            table[2][0] == "X" and table[2][1] == "X" and table[2][2] == "X" or \
            table[0][0] == "X" and table[1][0] == "X" and table[2][0] == "X" or \
            table[0][1] == "X" and table[1][1] == "X" and table[2][1] == "X" or \
            table[0][2] == "X" and table[1][2] == "X" and table[2][2] == "X" or \
            table[0][0] == "X" and table[1][1] == "X" and table[2][2] == "X" or \
            table[0][2] == "X" and table[1][1] == "X" and table[2][0] == "X":
        print("X won")
        print(table)
        break
    elif table[0][0] == 0 and table[0][1] == 0 and table[0][2] == 0 or \
            table[1][0] == 0 and table[1][1] == 0 and table[1][2] == 0 or \
            table[2][0] == 0 and table[2][1] == 0 and table[2][2] == 0 or \
            table[0][0] == 0 and table[1][0] == 0 and table[2][0] == 0 or \
            table[0][1] == 0 and table[1][1] == 0 and table[2][1] == 0 or \
            table[0][2] == 0 and table[1][2] == 0 and table[2][2] == 0 or \
            table[0][0] == 0 and table[1][1] == 0 and table[2][2] == 0 or \
            table[0][2] == 0 and table[1][1] == 0 and table[2][0] == 0:
        print("Y won")
        print(table)
        break
    else:
        count_ones = sum(cell == 1 for row in table for cell in row)
        if count_ones == 3:
            print("No winner")
            print(table)
            break
        else:
            continue

    # if table[starter_row][starter_col] == "X":
    #     print("Cell is already occupied")
    # else:
    #     table[starter_row][starter_col] = "O"
