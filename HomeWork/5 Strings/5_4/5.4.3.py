stroka = input('Введите текст: ')

count = 0
for sym in stroka:
    if sym.islower():
        count += 1
    else:
        count += 0

if count > len(stroka) / 2:
    print(stroka.lower())
else:
    print(stroka.upper())