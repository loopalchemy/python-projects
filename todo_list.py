import os

TASKS_FILE = "tasks.txt"
tasks = []

# Load tasks from file if it exists
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r") as f:
        for line in f:
            task_text, completed = line.strip().split("||")
            tasks.append({"task": task_text, "completed": completed == "True"})

def save_tasks():
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task['task']}||{task['completed']}\n")

def show_menu():
    print("\nTo-Do List Menu")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks()
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. {task['task']} [{status}]")

def complete_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        save_tasks()
        print("Task marked as completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

       
