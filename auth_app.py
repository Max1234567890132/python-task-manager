# Сколько чисел будем вводить
n = int(input("Сколько чисел? "))

# Ввод первого числа
num = float(input("Введите число 1: "))
max_number = num  # наибольшее
min_number = num  # наименьшее
sum_numbers = num # для среднего

# Цикл для оставшихся чисел
for i in range(2, n + 1):
    num = float(input(f"Введите число {i}: "))
    sum_numbers += num           # суммируем для среднего
    if num > max_number:
        max_number = num         # обновляем максимум
    if num < min_number:
        min_number = num         # обновляем минимум

# Выводим результаты
print("Наибольшее число:", max_number)
print("Наименьшее число:", min_number)
print("Среднее арифметическое:", sum_numbers / n)
