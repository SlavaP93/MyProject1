import random

team_1 = [round(random.uniform(5.0,10.0), 2) for _ in range(20)]
team_2 = [round(random.uniform(5.0,10.0), 2) for _ in range(20)]
print(f'Первая команда: {team_1}')
print(f'Вторая команда: {team_2}')
resault = [team_1[win] if team_1[win] > team_2[win] else team_2[win] for win in range(20)]
print(f'Команда победителей: {resault}')
