def load_products(filename):
    products = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                name, amount = line.strip().split(": ")
                products[name.capitalize()] = int(amount)
    except FileNotFoundError:
        print("File not found")

    return products


def add_products(products):
    name = input("name please: ").strip()

    if name.lower() == "stop":
        return "stop"

    name = name.capitalize()

    try:
        amount = int(input("amount please: "))
    except ValueError:
        print("only numbers allowed")
        return

    if amount < 0:
        print("amount must be positive")
        return

    products[name] = products.get(name, 0) + amount


products = load_products("products.txt")

while True:
    result = add_products(products)
    if result == "stop":
        break

print(products)
