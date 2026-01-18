for _ in range(3):
    name = input("Имя игрока: ").capitalize()
    points = int(input("Сколько очков добавить: "))
    players[name] = players.get(name, 0) + points
    print(players)