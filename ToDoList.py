
todo = []
choice = 0


def show_task():
    while True:
        if not todo:
            print("No tasks in the list to show \n")
            break
        else:
            for i in range(len(todo)):
                print(i + 1, ". ", todo[i])
            break


def add_task():
    task = input("Create a new task: ")
    todo.append(task)
    print("Task added")


def remove_task():
    while True:
        if not todo:
            print("No task to remove")
        else:
            if not todo:
                print("No tasks in the list to remove")
                break
            else:
                print("List of tasks: ")
                for i in range(len(todo)):
                    print(i + 1, ". ", todo[i])
            rem_task = int(input("\nEnter the task number for removing: "))
            print(todo[rem_task - 1], " has been removed!")
            todo.remove(todo[rem_task - 1])
            break


while True:
    print("\nToDo List Menu: ")
    print("1. View Tasks \n"
          "2. Add a Task \n"
          "3. Remove a Task \n"
          "4. Exit \n")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            if choice == 1:
                show_task()
            if choice == 2:
                add_task()
            if choice == 3:
                remove_task()
            if choice == 4:
                print("End of program")
                break
        else:
            raise ValueError
    except ValueError:
        print("Invalid choice ")
        continue


