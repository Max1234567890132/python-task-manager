list = {"max":1, "a":2}

while True:
    num = input("number")
    if num ==0:
        break

    b = {"max":1, "a":2}
    if b is None:
        print("not")
    else:
        print("ja",b)