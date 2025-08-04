# print("ToDo List Menu: ")
# print("1. View Tasks \n"
#       "2. Add a Task \n"
#       "3. Remove a Task \n"
#       "4. Exit \n")

todo = []
choice = 0
while True:
    print("ToDo List Menu: ")
    print("1. View Tasks \n"
          "2. Add a Task \n"
          "3. Remove a Task \n"
          "4. Exit \n")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            print(" ")
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice \n")
        continue

    if choice == 1:
        if not todo:
            print("No tasks in the list to show \n")
            continue
        else:
            for i in range(len(todo)):
                print(i+1,". ", todo[i])
        continue

    if choice == 2:
        task = input("Create a new task: ")
        todo.append(task)
        print("\n")

    if choice == 3:
        if not todo:
            print("No task to remove")
        else:
            if not todo:
                print("No tasks in the list to remove")
                continue
            else:
                print("List of tasks: ")
                for i in range(len(todo)):
                    print(i + 1, ". ", todo[i])
            rem_task = int(input("\nEnter the task number for removing: "))
            print(todo[rem_task-1], " has been removed!")
            todo.remove(todo[rem_task - 1])

    if choice == 4:
        print("End of program")
        break
