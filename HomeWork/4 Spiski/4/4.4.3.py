import random

N = int(input('Введите кол-во чисел: '))
spisok = [random.randint(0, 100) for _ in range(N + 1)]
print(spisok)
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
new_num = spisok[0:a-1]
new_num.extend(spisok[b-1:])
print(new_num)