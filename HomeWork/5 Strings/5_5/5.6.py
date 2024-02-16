text = input('Введите строку: ')
count = 1
latter = []
for i in range(len(text)):
    if text[i] == text[count + 1:count + 2]:
        count += 1
        continue
    latter.append(''.join([text[i], str(count)))
print(latter)