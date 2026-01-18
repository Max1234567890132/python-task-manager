# 1. Словарь с пользователями
users = {
    1: {"name": "Max", "age": 30},
    2: {"name": "Anna", "age": 25}
}

# 2. Спрашиваем, что хочет сделать пользователь
action = input("Выберите действие: update / delete: ").lower()

# 3. Спрашиваем id пользователя
user_id = int(input("Введите id пользователя: "))

# 4. Логика действий
if action == "update":
    # TODO: спросить новый возраст и обновить
    pass
elif action == "delete":
    # TODO: удалить пользователя
    pass
else:
    print("Неизвестное действие")

# 5. Вывод всех пользователей
print(users)
