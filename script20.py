def add_player(players):
    name = input("Имя: ").capitalize()

    try:
        points = int(input("Очки: "))
    except ValueError:
        print("Ошибка: очки должны быть числом")
        return

    if points > 10:
        print("🎉 Бонус!")

    players[name] = players.get(name, 0) + points


def show_result(players):
    print("\nРезультат:")
    for name, points in players.items():
        print(name, "→", points)

    print("Всего очков:", sum(players.values()))

players = {}

for _ in range(3):
    add_player(players)

show_result(players)