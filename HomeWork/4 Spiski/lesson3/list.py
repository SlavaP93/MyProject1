S = input('Введите строку: ')
sym_s = list(S)
zamen = input('Какой символ нужно заменить? ')
sym_zamen = input('На какой заменить? ')
count_index = -1
count = 0
for i in sym_s:
    count_index += 1
    if i == zamen:
        sym_s[count_index] = sym_zamen
        count += 1
else:
    print('Нет символов для замен')
new_s = ''
for i_2 in sym_s:
    new_s += i_2

print(new_s)
print('замен символов',zamen,'на',sym_zamen,'было',count,'раз')