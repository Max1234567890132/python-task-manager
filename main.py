user_data = {
    "username": "admin",
    "password": "123"
}

def login(username, password):
    if username == user_data["username"] and password == user_data["password"]:
        return True
    else:
        return False


username = input("Username: ")
password = input("Password: ")

print(login(username, password))