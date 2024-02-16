def func_ind(string):
    spisok = []
    if isinstance(string,str) is False:
        for ind, sym in enumerate(string):
            sym = str
    for index, sym in enumerate(string):
        if index % 2 == 0:
            spisok.append(sym)


    return spisok

# text = input('Введите строку: ')
text = [100, 200, 300, 'буква', 0, 2, 'а']
print(func_ind(text))