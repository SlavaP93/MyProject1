guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    guests_count = len(guests)
    print(f'Сейчас на вечеринке {guests_count} человек {guests}')
    comand = input('Человек пришёл или ушёл? ')
    if comand == 'пришёл':
        new_name = input('Имя гостя? ')
        if guests_count < 6:
            guests.append(new_name)
            print(f'Привет, {new_name}!')
        else:
            print(f'Простите {new_name}, мест нет!')
    if comand == 'ушёл':
        name_out = input('Имя гостя? ')
        guests.remove(name_out)
    if comand == 'пора спать':
        print(guests,' Спокойной ночи!')
        break
