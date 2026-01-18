players = {}
for player in range(2):
    name = input("name").capitalize()
    points = int(input("points"))
    if points >10:
        print("Бонус!")
    players[name] = players.get(name,0) + points
    total = sum(players.values())

print(players)
print(total)