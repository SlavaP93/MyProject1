roliki = [39, 40, 41, 41, 42, 43]
N = int(input('Кол-во людей: '))
visitors = []
for i in range(N):
    visitors.append(int(input(F'Какой размер у {i + 1} человека? ')))
visit_rol = 0
for rol in roliki:
    for razm in visitors:
        if rol == razm:
            visit_rol += 1
            roliki.remove(rol)
print('Обутых поситителей: ',visit_rol)
print('ролики остались',roliki)