import json
import os

# Загрузка данных
if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        users = json.load(file)
    # приводим ключи к int, если нужно
    users = {int(k): v for k, v in users.items()}
else:
    users = {}

while True:
    action = input("add / show / update / delete / exit: ").lower()

    # --- ADD ---
    if action == "add":
        name = input("Name: ")
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Only numbers allowed")
            continue

        if age < 18:
            print("Too young")
            continue

        new_id = max(users.keys()) + 1 if users else 1
        users[new_id] = {"name": name, "age": age}
        print(f"User added with id {new_id}")

    # --- SHOW ---
    elif action == "show":
        if not users:
            print("No users yet")
        else:
            for uid, data in users.items():
                print(uid, data["name"], data["age"])

    # --- UPDATE ---
    elif action == "update":
        try:
            uid = int(input("ID to update: "))
        except ValueError:
            print("ID must be a number")
            continue

        if uid not in users:
            print("User not found")
            continue

        try:
            new_age = int(input("New age: "))
        except ValueError:
            print("Age must be a number")
            continue

        users[uid]["age"] = new_age
        print(f"User {uid} updated")

    # --- DELETE ---
    elif action == "delete":
        try:
            uid = int(input("ID to delete: "))
        except ValueError:
            print("ID must be a number")
            continue

        if uid in users:
            del users[uid]
            print(f"User {uid} deleted")
        else:
            print("User not found")

    # --- EXIT ---
    elif action == "exit":
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        print("Data saved. Exiting...")
        break

    else:
        print("Unknown command")
