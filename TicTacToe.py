import numpy as np

table = np.ones((3, 3), dtype=object)


def user_input(name):
    while True:
        print(f"player {name}'s turn: ")
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

    return [starter_row, starter_col]


def check_cells():
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
    elif table[0][0] == 0 and table[0][1] == 0 and table[0][2] == 0 or \
                table[1][0] == "Y" and table[1][1] == "Y" and table[1][2] == "Y" or \
                table[2][0] == "Y" and table[2][1] == "Y" and table[2][2] == "Y" or \
                table[0][0] == "Y" and table[1][0] == "Y" and table[2][0] == "Y" or \
                table[0][1] == "Y" and table[1][1] == "Y" and table[2][1] == "Y" or \
                table[0][2] == "Y" and table[1][2] == "Y" and table[2][2] == "Y" or \
                table[0][0] == "Y" and table[1][1] == "Y" and table[2][2] == "Y" or \
                table[0][2] == "Y" and table[1][1] == "Y" and table[2][0] == "Y":
            print("Y won")
            print(table)
    else:
            print(table)



control_list=[]
while True:
    print("Start: ")
    while True:
        x = user_input("X")
        row, col = x
        if x in control_list:
            print("Cell is already occupied")
            continue
        else:
            control_list.append(x)
            table[row][col] = "X"
        break

    while True:
        x = user_input("Y")
        row, col = x
        if x in control_list:
            print("Cell is already occupied")
            continue
        else:
            control_list.append(x)
            table[row][col] = "Y"
        break

    check_cells()
