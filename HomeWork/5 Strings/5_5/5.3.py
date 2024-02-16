file = input('Введите название файла с расширением: ')
form = ('.txt','.docx')
spec_sym = ('@', '№', '$', '%', '^', '&', '*','()')
if not file.endswith(form):
    print('Неверное расширение файла!')
elif file.startswith(spec_sym):
    print('Обнаружен недопустимый спец символ!')
else:
    print('загружен файл {}'.format(file))