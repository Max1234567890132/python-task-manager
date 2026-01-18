grades = {
    "Максим": 90,
    "Аня": 75,
    "Игорь": 60
}
for _ in range(3):
    name = input("Введите имя ученика: ")
    print("Оценка:", grades.get(name, "Такого ученика нет"))

