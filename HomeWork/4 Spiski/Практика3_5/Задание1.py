first = [1, 5, 3]
second = [1, 5, 1, 5]
third = [1, 3, 1, 5, 3, 3]
first.extend(second)
print('Кол-во 5 при первом объединении: ',first.count(5))
main_spisok = []
for _ in range(first.count(5)):
    first.remove(5)
main_spisok.extend(first)
main_spisok.extend(third)
print('Кол-во 3 при втором объединении: ',main_spisok.count(3))
print('Итоговый список: ',main_spisok)
