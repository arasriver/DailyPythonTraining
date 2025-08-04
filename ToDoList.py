
todo = []
choice = 0
FILE_NAME = "todo.txt"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    todo.append(task)
    except FileNotFoundError:
        pass


def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in todo:
            file.write(task + "\n")


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
    save_tasks()
    print("Task added")


def remove_task():
    if not todo:
        print("No tasks in the list to remove")
        return
    print("List of tasks: ")
    for i in range(len(todo)):
        print(i + 1, ". ", todo[i])
    try:
        rem_task = int(input("\nEnter the task number to remove: "))
        if 1 <= rem_task <= len(todo):
            save_tasks()
            print(todo[rem_task - 1], "has been removed!")
            todo.pop(rem_task - 1)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


while True:
    print("\nToDo List Menu: ")
    print("1. View Tasks \n"
          "2. Add a Task \n"
          "3. Remove a Task \n"
          "4. Exit \n")
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                show_task()
            case 2:
                add_task()
            case 3:
                remove_task()
            case 4:
                print("End of program")
                break
    except ValueError:
        print("Invalid choice ")
        continue


