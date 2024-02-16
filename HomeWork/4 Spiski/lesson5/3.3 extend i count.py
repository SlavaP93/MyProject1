massage_1 = []
massage_2 = []
massage_1.append(input('Введите сообщение 1: '))
massage_2.append(input('Введите сообщение 2: '))
massage_3 = ''
sym_1 = []
for i in massage_1:
    sym_1 += i
sym_2 = []
for i_2 in massage_2:
    sym_2 += i_2
sym_summ_1 = sym_1.count('!') + sym_1.count('?')
sym_summ_2 = sym_2.count('!') + sym_2.count('?')
if sym_summ_1 > sym_summ_2:
    sym_1.extend(sym_2)
    for k in sym_1:
        massage_3 += k
    print(massage_3)
elif sym_summ_1 < sym_summ_2:
    sym_2.extend(sym_1)
    for k in sym_2:
        massage_3 += k
    print(massage_3)
else:
    print('Ой!')