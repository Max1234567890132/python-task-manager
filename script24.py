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


def show_products(products):
    for name, amount in products.items():
        print(name, amount)


def save_products(products, filename):
    with open(filename,'w', encoding='utf-8') as f:
        for name, amount in products.items():
            f.write(f"{name}: {amount}\n")



FILENAME = "products.txt"

products = load_products(FILENAME)

while True:
    print("1-add products:")
    print("2-show")
    print("0-exit ")

    choice = input("choice: ")

    if choice == "1":
        add_products(products)
    if choice == "0":
        break
    if choice == "2":
        show_products(products)


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