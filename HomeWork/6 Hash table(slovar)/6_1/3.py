contact_book = dict()
while True:
    print('Текущие контакты в телефоне:\n')
    for i in contact_book:
        print(i,':',contact_book[i])
    name = input('Введите имя контакта: ')
    if name in contact_book:
        print('Такое имя уже есть в контактах!')
        break
    number = int(input('Введите номер телефона: '))
    contact_book[name] = number