n = int(input('Введите количество чисел в списке: '))
spisok = []
for _ in range(n):
    spisok.append(int(input('Введите число списка: ')))
k = int(input('Введите делитель: '))
ind = -1
ind_sum = 0
for i in spisok:
    ind += 1
    if i % k == 0:
        print('Индекс числа ',i,':', ind )
        ind_sum += ind
print('Сумма индексов: ', ind_sum)

