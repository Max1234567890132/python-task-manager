tasks = []

def add_task(tasks):
    task = input("Введите задачу: ")
    tasks.append(task)

def show_tasks(tasks):
    if not tasks:
        print("Задач нет")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def remove_task(tasks):
    if not  tasks:
        print("Задач нет")
        return

    show_tasks(tasks)

    number = int(input("Введите номер задачи для удаления"))

    if 1 <= number <= len(tasks):
        removed = tasks.pop(number -1)
        print("Удалена задача:", removed)
    else:
        print("Неверный номер")

def save_tasks(tasks):
    with open("tasks.txt", "w",encoding= "utf-8" ) as file:
        for task in tasks:
            file.write(task + "\n")

        print("Задачи сохранены")

def load_tasks():
    try:
        with open("tasks.txt","r", encoding= "utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []




while True:
    print("\nМеню:")
    print("1 — добавить задачу")
    print("2 — удалить задачу")
    print("3 — показать все задачи")
    print("4 — сохранить задачи в файл")
    print("5 — загрузить задачи при старте")
    print("6 — выход")

    choice = input("Выбор: ")

    if choice == "1":
        add_task(tasks)
    if choice == "3":
        show_tasks(tasks)
    if choice == "2":
        remove_task(tasks)
    if choice == "4":
        save_tasks(tasks)
    if choice == "5":
        load_tasks()

    if choice == "6":
        break
