def film_f(new, film_list):
    for i in film_list:
        if i == new:
            return True
    return False


def film_2(new, film_list):
    for i in film_list:
        if i == new:
            return False
    return True


films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица', '1'
]
new_film = ['Проклятый остров', 'Начало', 'Матрица', '1']
while True:
    print(new_film)
    add = input('Введите название фильма: ')
    if film_f(add, films):
        comand = input('\nКоманды: добавить, вставить, удалить: ')
        if comand == 'добавить':
            if film_2(add, new_film):
                new_film.append(add)
            else:
                print('Такой фильм уже есть в вашем списке.')
        if comand == 'вставить':
            ind = int(input('на какое место?: '))
            new_film.insert(ind - 1, add)
        if comand == 'удалить':
            if film_f(add, new_film):
                new_film.remove(add)
    else:
        print('Такого фильма нет в рейтинге!')