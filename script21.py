products = {}

total_amount = 0

for i in range(3):
    name_products = input("Название товара: ").capitalize()

    try:
        amount = int(input("Количество: "))
    except ValueError:
        print("Только число!")
        continue

    products[name_products] = products.get(name_products, 0) + amount
    total_amount += amount

print(products)
print("Общее количество товаров:", total_amount)
