import random

player = random.choice(list(players.keys()))
points = random.randint(1, 5)
players[player] += points
print(players)
