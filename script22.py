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
    name = input("Enter product name: ").strip()

    if name.lower() == "stop":
        return "stop"

    name = name.capitalize()

    try:
        amount = int(input("Enter product amount: "))
    except ValueError:
        print("Invalid input")
        return

    if amount < 0:
        print("Invalid input")
        return

    products[name] = products.get(name, 0) + amount


def save_products(products, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for name, amount in products.items():
            f.write(f"{name}: {amount}\n")


# ===== ОСНОВНАЯ ПРОГРАММА =====

FILENAME = "products.txt"

products = load_products(FILENAME)

while True:
    result = add_products(products)
    if result == "stop":
        break

save_products(products, FILENAME)

print("\nResult:")
total = 0
for name, amount in products.items():
    print(name, "→", amount)
    total += amount

print("Total:", total)
