import math

goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
fruit = input('Название фрукта: ')
price = int(input('Цена: '))
new_goods = [fruit, price]
goods.append(new_goods)
print(goods)
schet = 0
for i in goods:
    i[1] += i[1] * (8 / 100)
print('цена после повышения: ',goods)