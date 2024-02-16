N = int(input('Сколько контейнеров?: '))
raw_conteiners = []
for i in range(N):
    print('Введите вес контейнера',i + 1,':', end=' ')
    conteiner = int(input())
    if conteiner <= 200:
        raw_conteiners.append(conteiner)
print(raw_conteiners)
x = int(input('Введите вес нового контейнера: '))

for k in raw_conteiners:
    if x <= k:
        raw_conteiners.append(x)
    else:
        raw_conteiners.append(k)
print(raw_conteiners)

