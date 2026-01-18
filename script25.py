def load_products(filename):
    products = {}

    try:
        with open(filename,'r',encoding='utf-8') as f:
            for line in f:
                name, amount = line.strip().split(": ")
                products[name.capitalize()] = int(amount)
    except FileNotFoundError:
        print("File not found")

    return products

def add_product(products):
    name = input("Enter product name: ").strip()

    if name.lower() == "stop":
        return "stop"

    name = name.capitalize()


    try:
        amount = int(input("Enter product amount: "))
    except ValueError:
            print("only numbers allowed")
            return

    if amount <0:
        print("negative amount not allowed")
        return

    products[name] = products.get(name,0) +amount


def delete_product(products):
    name = input("Enter product name: ").strip()

    if name.lower() == "stop":
        return "stop"

    name = name.capitalize()

    if name not in products:
        print("product not found")
        return

    del products[name]
    print(f"{name}deleted ")


def show_products(products):
    for name, amount in products.items():
        print(f"{name}: {amount}")


def save_products(filename, products):
    with open(filename,'w',encoding='utf-8') as f:
        for name, amount in products.items():
            f.write(f"{name.capitalize()}: {amount}\n")


FILENAME = "products.txt"
products = load_products(FILENAME)


while True:
    print("1-add product")
    print("2-show products")
    print("3-delete product")
    print("4-save products")
    print("5-exit")

    choice = input("Enter choice: ")

    if choice == "1":
        result = add_product(products)
        if result == "stop":
            break

    elif choice == "2":
        show_products(products)

    elif choice == "3":
        result = delete_product(products)
        if result == "stop":
            break

    elif choice == "4":
        save_products(FILENAME, products)
        print("Saved")

    elif choice == "5":
        save_products(FILENAME, products)
        break

    else:
        print("Invalid choice")


save_products(FILENAME, products)
print("\nResult:")
total = 0
for name, amount in products.items():
    print(name,">" ,amount)
    total += amount




print("total: ", total)
