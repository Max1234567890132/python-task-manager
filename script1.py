import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

# ---------------- загрузка пользователей ----------------
users = {}

if os.path.exists("users.txt"):
    with open("users.txt", "r") as file:
        for line in file:
            login, password = line.strip().split(":")
            users[login] = password

# ---------------- функции ----------------
def login_user():
    login = login_entry.get()
    password = login_password_entry.get()

    if login in users and users[login] == password:
        messagebox.showinfo("Успех", f"Добро пожаловать, {login}!")
        clear_entries()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")

def register_user():
    login = reg_login_entry.get()
    password = reg_password_entry.get()

    if login == "" or password == "":
        messagebox.showerror("Ошибка", "Заполните все поля")
        return

    if login in users:
        messagebox.showerror("Ошибка", "Пользователь уже существует")
        return

    users[login] = password

    # записываем в файл
    with open("users.txt", "a") as file:
        file.write(f"{login}:{password}\n")

    messagebox.showinfo("Успех", "Регистрация успешна!")
    clear_entries()

def clear_entries():
    login_entry.delete(0, tk.END)
    login_password_entry.delete(0, tk.END)
    reg_login_entry.delete(0, tk.END)
    reg_password_entry.delete(0, tk.END)

# ---------------- hover эффект ----------------
def on_enter(e):
    e.widget["background"] = "#2980b9"

def on_leave(e):
    e.widget["background"] = "#3498db"

# ---------------- окно ----------------
root = tk.Tk()
root.title("Система авторизации")
root.geometry("360x320")
root.resizable(False, False)
root.configure(bg="#2c3e50")

BTN_COLOR = "#3498db"
TEXT_COLOR = "white"

# ---------------- вкладки ----------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", pady=10)

# ---------------- вкладка ВХОД ----------------
login_frame = tk.Frame(notebook, bg="#2c3e50")
notebook.add(login_frame, text="Вход")

tk.Label(login_frame, text="Логин", fg=TEXT_COLOR, bg="#2c3e50").pack(pady=5)
login_entry = tk.Entry(login_frame)
login_entry.pack()

tk.Label(login_frame, text="Пароль", fg=TEXT_COLOR, bg="#2c3e50").pack(pady=5)
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.pack()

login_btn = tk.Button(login_frame, text="Войти", bg=BTN_COLOR, fg="white", width=20, command=login_user)
login_btn.pack(pady=20)
login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

# ---------------- вкладка РЕГИСТРАЦИЯ ----------------
reg_frame = tk.Frame(notebook, bg="#2c3e50")
notebook.add(reg_frame, text="Регистрация")

tk.Label(reg_frame, text="Новый логин", fg=TEXT_COLOR, bg="#2c3e50").pack(pady=5)
reg_login_entry = tk.Entry(reg_frame)
reg_login_entry.pack()

tk.Label(reg_frame, text="Новый пароль", fg=TEXT_COLOR, bg="#2c3e50").pack(pady=5)
reg_password_entry = tk.Entry(reg_frame, show="*")
reg_password_entry.pack()

reg_btn = tk.Button(reg_frame, text="Зарегистрироваться", bg=BTN_COLOR, fg="white", width=20, command=register_user)
reg_btn.pack(pady=20)
reg_btn.bind("<Enter>", on_enter)
reg_btn.bind("<Leave>", on_leave)

root.mainloop()


# ---------------- окно ----------------
root = tk.Tk()
root.title("Система авторизации")
root.geometry("360x300")
root.resizable(False, False)
root.iconbitmap("icon.ico")

BG_COLOR = "#2c3e50"
BTN_COLOR = "#3498db"
TEXT_COLOR = "white"

root.configure(bg=BG_COLOR)

# ---------------- вкладки ----------------
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", pady=10)

# ---------------- вкладка ВХОД ----------------
login_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(login_frame, text="Вход")

tk.Label(login_frame, text="Логин", fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=5)
login_entry = tk.Entry(login_frame)
login_entry.pack()

tk.Label(login_frame, text="Пароль", fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=5)
login_password_entry = tk.Entry(login_frame, show="*")
login_password_entry.pack()

login_btn = tk.Button(
    login_frame,
    text="Войти",
    bg=BTN_COLOR,
    fg="white",
    width=20,
    command=login_user
)
login_btn.pack(pady=20)

login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

# ---------------- вкладка РЕГИСТРАЦИЯ ----------------
reg_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(reg_frame, text="Регистрация")

tk.Label(reg_frame, text="Новый логин", fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=5)
reg_login_entry = tk.Entry(reg_frame)
reg_login_entry.pack()

tk.Label(reg_frame, text="Новый пароль", fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=5)
reg_password_entry = tk.Entry(reg_frame, show="*")
reg_password_entry.pack()

reg_btn = tk.Button(
    reg_frame,
    text="Зарегистрироваться",
    bg=BTN_COLOR,
    fg="white",
    width=20,
    command=register_user
)
reg_btn.pack(pady=20)

reg_btn.bind("<Enter>", on_enter)
reg_btn.bind("<Leave>", on_leave)

root.mainloop()
