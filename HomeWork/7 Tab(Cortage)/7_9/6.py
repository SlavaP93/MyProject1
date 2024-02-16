phone_book = {('Иван', 'Иванов'): 62835628582, ('Иван', 'Петров'): 734673826832, ('Леха', 'Прыщ'): 654387628756}
while True:
    print(phone_book)
    option = int(input('Выберите действие: 1 - добавить, 2 - поиск: '))
    if option == 1:
        name = input('Введите фамилию и имя: ').lower().split()
        number = int(input('Введите номер телефона: '))
        if tuple(name) in phone_book:
            print('Такой контакт уже есть в списке!')
            quit(name)
        phone_book[tuple(name)] = number
    if option == 2:
        serch = input('Введите имя или фамилию: ')
        for i_num in phone_book:
            if serch == i_num[0] or serch == i_num[1]:
                print(' '.join(i_num), phone_book.get(i_num))
                continue

    else:
        print('Ошибка выбора.')