players = {
    "Max": 10,
    "Anna": 15
}

name = input("Имя игрока: ")
points = int(input("Сколько очков добавить: "))


players[name] = players.get(name, 0) + points
print(players)
