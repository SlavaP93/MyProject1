import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

mnoj = set(nums_1)
mnoj_2 = set(nums_2)
mnoj.remove(min(mnoj))
mnoj_2.remove(min(mnoj_2))
mnoj.add(random.randint(100,200))
mnoj_2.add(random.randint(100,200))

print(mnoj)
print(mnoj_2)

print('Объединение:', mnoj.union(mnoj_2))
print('Пересечение:', mnoj.intersection(mnoj_2))
print('Входящии только во второе множество:', mnoj_2.difference(mnoj))