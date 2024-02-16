import random

group_1 = [random.randint(50, 80) for _ in range(10)]
group_2 = [random.randint(30, 50) for _ in range(10)]

damage_monsters = [('Погиб' if group_2[damage] + group_1[damage] > 100 else 'ещё жив')
                   for damage in range(10)]
print(damage_monsters)
