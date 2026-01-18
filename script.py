num = int(input("Enter a number: ")) 
favorite_numbers = [1, 2, 3, 4, 5]

if num == 0:
    print("Ноль")
elif num in favorite_numbers:
    print("Это моё любимое число!")
elif num > 0 and num % 2 == 0:
    print("положительное чётное")
elif num > 0 and num % 2 != 0:
    print("положительное нечётное")
elif num < 0 and num % 2 == 0:
    print("отрицательное чётное")
else:
    print("отрицательное нечётное")