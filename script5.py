products = {}

def add_product(products):
    num = input("number of producks:")
    count = int(input("now mene producks:"))
    products[num] = products.get(num,0)+count
    print("Товар добавлен")
