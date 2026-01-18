from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# ----------------------------
# Загрузка пользователей из JSON при старте
# ----------------------------
if os.path.exists("users.json"):
    with open("users.json", "r") as file:
        users = json.load(file)
        # JSON возвращает ключи как строки, а нам нужны числа
        users = {int(k): v for k, v in users.items()}
else:
    users = {}

# ----------------------------
# Главная страница
#

# PUT /users/<id> — обновление пользователя
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        if user_id not in users:
            return jsonify({"error": "User not found"}), 404

        data = request.get_json()
        if not data or "name" not in data or "age" not in data:
            return jsonify({"error": "Missing name or age"}), 400

        # Обновляем пользователя
        users[user_id] = {
            "name": data["name"],
            "age": data["age"]
        }

        # Сохраняем изменения
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        return jsonify(users[user_id]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "API is working"

# ----------------------------
# GET /users — показать всех
# ----------------------------
@app.route("/users")
def get_users():
    try:
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------
# POST /users — добавить нового пользователя
# ----------------------------
@app.route("/users", methods=["POST"])
def add_user():
    try:
        data = request.get_json()
        if not data or "name" not in data or "age" not in data:
            return jsonify({"error": "Missing name or age"}), 400

        # Создаём уникальный id
        new_id = max(users.keys()) + 1 if users else 1
        users[new_id] = {
            "name": data["name"],
            "age": data["age"]
        }

        # Сохраняем в JSON
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        return jsonify(users[new_id]), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------
# DELETE /users/<id> — удалить пользователя
# ----------------------------
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        if user_id in users:
            deleted_user = users.pop(user_id)

            # Сохраняем изменения
            with open("users.json", "w") as file:
                json.dump(users, file, indent=4)

            return jsonify({"message": "User deleted", "user": deleted_user}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------
# Запуск сервера
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)

