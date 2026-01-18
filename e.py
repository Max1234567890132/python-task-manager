

num = int(input("number?"))

if  num > 0 and num % 2 == 0:
    print(" четное ")

elif num > 0 and num % 2 != 0:
    print("положительная четное")

elif num < 0 and num % 2 == 0:
    print("отрицательная четное ")

else:
    print("отрицательная не четное")

num1 = int(input("number?"))
num2 = int(input("number?"))
num3 = int(input("number?"))

if num1 >= num2 and num1 >= num3:
    print("наибольщее", num1)

elif num2 >= num1 and num2 >= num3:
    print("наибольщее", num2)

else:
    print("наибольщее", num3)



while True:
    try:
        num1 = int(input("number?"))
        num2 = int(input("number?"))
        print("1-number?",num1+num2)
        print("2-number?",num1-num2)
        print("3-number?",num1*num2)
        print("4-number?",num1/num2)
    except ZeroDivisionError:
        print("Деление на ноль невозможно")

    choice = input("Выбор")

    if choice == "1":
        result = num1 + num2
        print(result)
    elif choice == "2":
        result = num1 - num2
        print(result)
    elif choice == "3":
        result = num1 * num2
        print(result)
    elif choice == "4":
        result = num1 / num2
        print(result)


