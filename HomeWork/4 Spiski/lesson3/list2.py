s = input('Введите строку: ')
sym_s = list(s)
index_input = int(input('Введите номер символа '))
count_index = -1
print()
for i in sym_s:
    count_index += 1
    if count_index == index_input:
        print('символ слева:',sym_s[index_input - 2])
        print('символ справа',sym_s[index_input])
        if sym_s[index_input] == sym_s[index_input + 1] or sym_s[index_input] == sym_s[index_input - 1]:
            print()
            print('есть такой же символ')
            break
else:
    print()
    print('таких же символов нет')