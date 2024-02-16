phone_book = dict()
while True:
    print(phone_book)
    name = input('Введите фамилию и имя: ').split()
    number = int(input('Введите номер телефона: '))
    if tuple(name) in phone_book:
        print('Такой контакт уже есть в списке!')
        quit(name)
    phone_book[tuple(name)] = number
