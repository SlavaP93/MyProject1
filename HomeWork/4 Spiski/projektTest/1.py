N = int(input('Сколько контейнеров? '))
raw_conteiners = []
conteiner = 0
for i in range(N):
    print('Введите вес контейнера', i + 1,':', end=' ')
    conteiner = int(input())
    if conteiner <= 200:
        raw_conteiners.append(conteiner)
    else:
        print('контейнер не может весить больше 200!')
        break
print(raw_conteiners)

x = int(input('Вес нового контейнера: '))
new_index = 0
new_raw = []
while x < raw_conteiners[new_index]:
        new_raw.append(raw_conteiners[new_index])
        new_index += 1
print('Место нового контейнера: ',new_index + 1)
new_raw.append(x)
k = len(raw_conteiners)
while new_index != k:
    new_raw.append(raw_conteiners[new_index])
    new_index += 1
print(new_raw)


