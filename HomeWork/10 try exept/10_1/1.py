BRUCE_WILLIS = 42

try:
    input_data = input('Введите строку: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')
except IndexError:
    print('Строка слишком мала')
except ValueError:
    print('Ошибка ввода')
except:
    print('Неизвестная ошибка')
