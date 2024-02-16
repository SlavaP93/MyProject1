def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict



text = input('Введите текст: ').lower()
hist = histogram(text)
print('Оригинальный словарь частот: ',hist)
new_hist = dict()

for num in hist.values():
    sym_hist = []
    new_hist[num] = sym_hist
    for sym in hist.keys():
        if hist.get(sym) == num:
            sym_hist.append(sym)
print('Отсортированный список:')
for key in sorted(new_hist):
    print(key,':',new_hist.get(key))