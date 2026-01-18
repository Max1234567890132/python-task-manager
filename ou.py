def input_number(prompt= "Введите число:" ):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Введите только число.")


def check_event():
    num = input_number("Введите число:")
    if num == 0:
        print("четное ")
    else:
        print("не четное ")

def max_of_three():
    a = int(input("Число 1:"))
    b = int(input("Число 2:"))
    c = int(input("Число 3:"))
    if a >= b and a >=c:
        print("Наибольшее",a)
    elif b >= a and b >= c:
        print("Наибольшее",b)
    else:
        print("Наибольшее",c)

def arithmetic():
    x = input_number("Число 1",)
    y = input_number("Число 2",)
    print("Сумма:", x + y)
    print("Разность:", x - y)
    print("Произведение:", x * y)
    try:
        print("Деление:", x / y)
    except ZeroDivisionError:
        print("Деление на ноль невозможно")

def event_add_count():
    n = int(input_number("Сколько чисел хотите ввести?"))
    even_count = 0
    odd_count = 0
    for i in range(n):
        num = input_number(f"Введите число {i+1}: ")
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        print("Чётных чисел:",even_count)
        print("Нечётных чисел",odd_count)
while True:
    print("\nМеню тренажёра Python:")
    print("1 - Проверка чётности числа")
    print("2 - Наибольшее из трёх чисел")
    print("3 - Арифметика")
    print("4 - Счёт чётных и нечётных чисел")
    print("5 - Выход")

    choice = input("Выбор:")

    if choice == "1":
        check_event()
    elif choice == "2":
        arithmetic()
    elif choice == "3":
        event_add_count()
    elif choice == "4":
        max_of_three()
    elif choice == "5":
        print("Пока! Отличной тренировки завтра :)")
        break
    else:
        print("Неправильный выбор. Попробуйте снова")