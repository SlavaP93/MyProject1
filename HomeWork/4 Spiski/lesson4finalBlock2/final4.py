films = ['Крепкий орешек','Назад в будущее','Таксист','Леон','Богемская рапсодия','Город грехов','Мементо','Отступники','Деревня']
N = int(input('Сколько фильмов в списке?: '))
new_film = []
for _ in range(N):
    new = (input('Введите желаемый фильм: '))
    for i in films:
        if i == new:
            new_film.append(new)
            break
    else:
        print('Ошибка! такого фильма нет в списке!')
print('В вашем списке: ',new_film)
