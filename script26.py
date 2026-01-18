FILENAME = "tasks.txt"

# список задач
tasks = []

# -----------------------------
# функции
# -----------------------------

def load_tasks(filename):
    global tasks
    tasks = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if " | " in line:
                    title, status = line.split(" | ")
                    tasks.append({"title": title, "status": status})
    except FileNotFoundError:
        print("File not found, starting with empty task list.")

def save_tasks(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for task in tasks:
            f.write(f"{task['title']} | {task['status']}\n")
    print("Tasks saved!")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['title']} [{task['status']}]")

def add_task():
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return
    tasks.append({"title": title, "status": "open"})
    print(f"Task '{title}' added.")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

def mark_task_done():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]['status'] = 'done'
            print(f"Task '{tasks[num - 1]['title']}' marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")

# -----------------------------
# программа
# -----------------------------

load_tasks(FILENAME)

while True:
    print("\n--- TODO Manager ---")
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Mark task as done")
    print("4 - Delete task")
    print("5 - Save tasks")
    print("0 - Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        save_tasks(FILENAME)
    elif choice == "0":
        save_tasks(FILENAME)
        print("Exiting. Bye!")
        break
    else:
        print("Invalid choice. Try again.")
