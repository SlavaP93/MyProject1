violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}

num = int(input('Введите количество песен: '))
songs = input('Введите название песен через пробел: ').split()
count = 0

for i in range(num):
    for song in violator_songs:
        if violator_songs.get(songs[i]):
            count += violator_songs.get(songs[i])
        break
print(count)