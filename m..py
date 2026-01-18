import json

def load_tasks():
    try:
        with open("tasks.json", "r") as infile:
            return json.load(infile)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile, indent=2)

def add_task(tasks, title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)
    return tasks


def show_tasks(tasks):
    for i , task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[]"
        print(f"{i}. {task['title']} | {status}")

while True:
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tasks = load_tasks()
        title = input("Task title: ")
        tasks = add_task(tasks, title)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        tasks = load_tasks()
        show_tasks(tasks)

    elif choice == "3":
        break

    else:
        print("Invalid choice")