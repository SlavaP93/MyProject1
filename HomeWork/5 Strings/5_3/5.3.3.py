names = input('Введите имя и фамилию через , : ').split(',')
age = input('Сколько исполнилось?: ').split()

name = [ind for ind in names]
ages = [hb for hb in age]

for index in range(len(names)):
    resault = 'С днём рождения {i_name}!!! С {i_age}-летием тебя!!!'.format(
        i_name=name[index],
        i_age=ages[index])
    print(''.join(resault))
