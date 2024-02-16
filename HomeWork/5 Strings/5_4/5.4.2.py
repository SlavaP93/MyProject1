part = input('Введите диск: ').upper()
file = input('Введите название файла с расширением: ')

path = '{disk}:/user/docs/folder/{name}'.format(
    disk=part,
    name=file
)

if not part.startswith('C'):
    print('Ошибка! Выберите диск С! ')
elif not file.endswith('.txt'):
    print('Ошибка! Формат файла должен быть .txt')
else:
    print(path)