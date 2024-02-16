def high_perc(perc, price):
    return round(price * (1 + perc / 100), 2)

spisok = [2.22, 5.67, 40.5, 23.08, 1.66]
first = int(input('На сколько повышаем первый год?:'))
secod = int(input('На сколько повышаем второй год?: '))

first_year = [high_perc(first, i_price) for i_price in spisok]
secod_year = [high_perc(secod, i_price) for i_price in first_year]

print(first_year)
print(secod_year)