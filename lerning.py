while True:
    print(" 1 - Привет")
    print(" 2 - Выход")
    print(" 3 - Сложение")
    print(" 4 - Деление")
    print(" 5 — Умножение")

    choice = input("Выбор")

    if choice == "1":
        print("Привет")
    elif choice == "3":
        num = float(input("видите число"))
        num2 = float(input("видите число"))
        result = num + num2
        print("Сложение",result)
    elif choice == "4":
       num = float(input("видите число"))
       num2 = float(input("видите число"))
       if num2 != 0:
           result = num / num2
           print("Деление",result)
       else:
           print("Деление на ноль невозможно")

    elif choice == "5":
        num = float(input("видите число"))
        num2 = float(input("видите число"))
        result = num * num2
        print("Умножение",result)

    elif choice == "2":
        print("Пока")
        break
    else:
        print("Неправильный выбор ")
        continue
