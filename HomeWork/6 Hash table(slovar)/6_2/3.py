text = input('Введите текст: ').lower()
hist = dict()

for sym in text:
    if sym in hist:
        hist[sym] += 1
    else:
        hist[sym] = 1

for i_sym in sorted(hist):
    print(i_sym,':',hist[i_sym])
print(max(hist.values()))