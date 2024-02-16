def musik(sum, seach, shop):
    for i in shop:
        if i[0] == seach:
            sum += i[1]
            return sum
    else:
        print('Такого товара нет')

violator_songs = [
['World in My Eyes', 4.86],
['Sweetest Perfection', 4.43],
['Personal Jesus', 4.56],
['Halo', 4.9],
['Waiting for the Night', 6.07],
['Enjoy the Silence', 4.20],
['Policy of Truth', 4.76],
['Blue Dress', 4.29],
['Clean', 5.83]
]

sum = 0
N = int(input('Сколько треков?: '))
for i in range(N):
    track = input('Введите название трека: ')
    sum = musik(sum, track, violator_songs)


print(sum)