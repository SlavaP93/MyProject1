incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

summa = 0
for i_inc in incomes.values():
    summa += i_inc
print(f'Общий доход: {summa}')

minimal = min(incomes.values())
for i in incomes.keys():
    if incomes[i] is minimal:
        print('Минимальный доход принес: {0} он принес {1}'.format(i,minimal))
        incomes.pop(i)
        break
print('Итоговый список:\n',incomes)