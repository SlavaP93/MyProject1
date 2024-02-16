try:
    stroka = input('Введите строку: ')
    text = open('answer.txt', 'w')
    text.write(stroka)
    text.close()
except TypeError:
    print('Ошибка ввода данных')
except OSError:
    print("Ошибка при открытии файла")
except BaseException:
    print("Неожиданная ошибка")
