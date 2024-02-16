while True:
    adress = input('Введите IP адресс: ').split('.')
    prov = ''
    for i in adress:
        if len(adress) != 4:
            print('Адрес — это четыре числа, разделённые точками.')
            break
        elif not i.isnumeric():
            print(f'{i} не является числом')
            break
        elif int(i) > 255:
            print(f'Число {i} превышает допустимое значение!')
            break
    else:
        print('.'.join(adress),'- корректный адресс')
        break
