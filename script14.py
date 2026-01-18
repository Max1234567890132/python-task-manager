players = {}


for i in range(3):
    name = input("name pless").capitalize()
    points = int(input("now meny points "))
    players[name] = players.get(name, 0) + points
    total = sum(players.values())

print(players)