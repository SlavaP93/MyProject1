N = int(input('Введите кол-во сотрудников в списке: '))
cash = []
for sotr in range(N):
    cash.append(int(input(f'Введите зарплату сотпудника ')))
print(cash)
for i in cash:
    if i == 0:
        cash.remove(i)
print('Осталось сотрудников: ', len(cash))
print(cash)
print('Max = ',max(cash))
print('Min = ',min(cash))