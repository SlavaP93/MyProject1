small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

big_storage.update(small_storage)

goods = input('Введите название товара: ')
no = None
if big_storage.get(goods) != no:
    print(big_storage.get(goods))
else:
    print('Такого товара нет!')