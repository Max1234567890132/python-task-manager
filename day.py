days = {1:"понедельник "}

def day_name(day):
    return days.get(day)

day = int(input(""))
print(day_name(day))

