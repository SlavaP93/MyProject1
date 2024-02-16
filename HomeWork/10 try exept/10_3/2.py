def func_ispalindrom(slovo):
    x = len(slovo)
    i = 0
    x = x - 1
    k = 0
    while x - i >= i:
        if slovo[x - i] == slovo[i]:
            i += 1
        else:
            k = 1
            break
    if k == 1:
        return True
    else:
        return False

text = open('words.txt','r')
count = 0
palindroms = []
try:
    for i_line in text:
        count += 1
        if func_ispalindrom(i_line):
            print(f'Палиндром в строке {count}')
            palindroms.append(i_line.removesuffix('\n'))
        for sym in i_line:
            if sym.isdigit():
                raise ValueError(open('error.log','w',encoding='utf-8').write(f'ошибка в строке {count}'))
finally:
    print(palindroms)


