text = input('Введите символы: ')
new = []
count = 0
k = 0
for i in range(len(text)):
    count += 1
    if text[i] == text[count:count+1]:
        k += 1
    else:
        new.append(text[i])
        new.append(str(k + 1))
        k = 0

print(''.join(new))