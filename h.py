import random

while True:
    print("1. Ввод чисел и подсчёт")
    print("2. Выход")
    print("3.мини игра ")

    choice = input("Выбор: ")




    if choice == "1":
        count = 0
        summa = 0

        while True:
            num = int(input("Введите число (0 — стоп): "))
            if num == 0:
                break
            count += 1
            summa += num

        print("Количество:", count)
        print("Сумма:", summa)

        guess = random.randint(1, 10)

        while True:
            num = int(input("numbers"))
            if guess == num:
                print("winn eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuoooooooooooooooooo gratuleshen ")
                break
            elif num < guess:
               print("Слишком мало")

            else:
                print("Слишком много")

    elif choice == "2":
        print("Выход из программы")
        break
    else:
        print("Неверный выбор")
