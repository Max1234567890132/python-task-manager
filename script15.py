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

    if choice == "6":
        break
