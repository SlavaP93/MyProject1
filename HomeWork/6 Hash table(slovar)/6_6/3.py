goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345':
        [{'quantity': 27,
          'price': 42},],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
count = 0
numb = ''
summ = 0

for i_goods in goods:
    if goods.get(i_goods) in store.keys():
        for i in range(len(store[goods.get(i_goods)])):
            count += store[goods.get(i_goods)][i]['quantity']
            summ += store[goods.get(i_goods)][i]['quantity'] * store[goods.get(i_goods)][i]['price']
        print(i_goods, '-',count,'-штук, общая стоимость:',summ)
    count = 0
    summ = 0