n = int(input('Введите количество сотрудников: '))
worker_ID = []
for _ in range(n):
    worker_ID.append(int(input('Введите ID: ')))

Seach = int(input('Какой сотрудник нужен? '))
s = 0
for i in worker_ID:
    if i == Seach:
        print('Сотрудник с ID:', i, ' На месте')
        break
else:
    print('Такого сотрудника нет')