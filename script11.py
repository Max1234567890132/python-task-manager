Действие	Код примера
Создать словарь игроков	                     players = {"Max":10, "Anna":15}
Взять очки игрока	                         print(players["Max"])
Сохранить очки в переменную	                 x = players["Max"]
Увеличить очки игрока	                     players["Max"] += 1
Добавить нового игрока	                     players["Bob"] = 5
Сумма всех очков	                         total = sum(players.values())
Увеличить очки через                         input()	name=input().capitalize(); points=int(input()); players[name]=players.get(name,0)+points
Несколько действий через цикл	             for _ in range(3): name=input().capitalize(); points=int(input()); players[name]=players.get(name,0)+points
Случайное увеличение очков	                 import random; player=random.choice(list(players.keys())); players[player]+=random.randint(1,5)