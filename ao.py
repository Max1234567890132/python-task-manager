# ======================
# Функции с обработкой ошибок
# ======================

def say_hello():
    print("Привет!")

def addition():
    try:
        num1 = float(input("Введите число 1: "))
        num2 = float(input("Введите число 2: "))
        print("Сумма:", num1 + num2)
    except ValueError:
        print("Ошибка! Нужно вводить только числа")

def division():
    try:
        num1 = float(input("Введите число 1: "))
        num2 = float(input("Введите число 2: "))
        result = num1 / num2
    except ValueError:
        print("Ошибка! Нужно вводить только числа")
    except ZeroDivisionError:
        print("Деление на ноль невозможно")
    else:
        print("Деление:", result)

def multiplication():
    try:
        num1 = float(input("Введите число 1: "))
        num2 = float(input("Введите число 2: "))
        print("Умножение:", num1 * num2)
    except ValueError:
        print("Ошибка! Нужно вводить только числа")

def max_number():
    try:
        n = int(input("Сколько чисел хотите ввести? "))
        if n <= 0:
            print("Ошибка! Нужно ввести положительное количество чисел")
            return
        num = float(input("Введите число 1: "))
        max_num = num
        for i in range(2, n + 1):
            num = float(input(f"Введите число {i}: "))
            if num > max_num:
                max_num = num
        print("Наибольшее число:", max_num)
    except ValueError:
        print("Ошибка! Нужно вводить только числа")

def even_odd_count():
    try:
        n = int(input("Сколько чисел хотите ввести? "))
        if n <= 0:
            print("Ошибка! Нужно ввести положительное количество чисел")
            return
        even_count = 0
        odd_count = 0
        for i in range(1, n + 1):
            num = int(input(f"Введите число {i}: "))
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        print("Чётных чисел:", even_count)
        print("Нечётных чисел:", odd_count)
    except ValueError:
        print("Ошибка! Нужно вводить только числа")

# ======================
# Главное меню программы
# ======================

while True:
    print("\nМеню программы:")
    print("1 - Привет")
    print("2 - Сложение")
    print("3 - Деление")
    print("4 - Умножение")
    print("5 - Наибольшее число")
    print("6 - Чётность чисел")
    print("7 - Выход")

    choice = input("Выбор: ")

    if choice == "1":
        say_hello()
    elif choice == "2":
        addition()
    elif choice == "3":
        division()
    elif choice == "4":
        multiplication()
    elif choice == "5":
        max_number()
    elif choice == "6":
        even_odd_count()
    elif choice == "7":
        print("Пока!")
        break
    else:
        print("Неправильный выбор. Попробуйте снова.")
