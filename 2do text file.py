import os

FILENAME = "TodoList.txt"

tasks = []


def load_tasks():
    """Load tasks from TodoList.txt into the tasks list, if the file exists."""
    if not os.path.exists(FILENAME):
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Format: "1::Task text"  (1 = done, 0 = not done)
            status, _, task_text = line.partition("::")
            tasks.append({"task": task_text, "done": status == "1"})


def save_tasks():
    """Save the current tasks list back to TodoList.txt."""
    with open(FILENAME, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "1" if task["done"] else "0"
            f.write(f"{status}::{task['task']}\n")


def show_menu():
    print("\n --- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks()
    print(f"Task '{task}' added!")


def view_task():
    if not tasks:
        print("No tasks yet")
        return
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{index}. {task['task']} [{status}]")


def mark_done():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks()
            print("Marked as done!")
        else:
            print("Invalid number")
    except ValueError:
        print("Please enter a valid number")


def delete_task():
    view_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"Deleted task: {removed['task']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number")


load_tasks()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
