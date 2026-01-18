def load_products(filename):
    products = {}

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                name, amount = line.strip().split(": ")
                products[name] = int(amount)
    except FileNotFoundError:
        print("File not found")

    return products

def add_product(products):
    name = input("Название товара: ").strip()

    if name.lower() == "stop":
        return "stop"

    name = name.capitalize()

    try:
        amount = int(input("Количество: "))
    except ValueError:
        print("Введите число")
        return

    if amount < 0:
        print("Количество не может быть отрицательным")
        return

    products[name] = products.get(name, 0) + amount


products = load_products("products.txt")

while True:
    result = add_product(products)
    if result == "stop":
        break

print(products)
