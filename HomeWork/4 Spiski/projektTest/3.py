slovo = input('Введите слово: ')
spisok = []
for i in slovo:
    spisok.append(i)
k = len(spisok) - 1
new_spisok = []
for _ in range(len(spisok)):
    new_spisok.append(spisok[k])
    k -= 1
new_slovo = ''
for i2 in new_spisok:
    new_slovo += i2

if new_slovo == slovo:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')