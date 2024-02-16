site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': "А вот здесь новый абзац"
            }
    }
}

def seach(dicti,word,n):
    if word in dicti:
        return dicti[word]
    for i_key in dicti.values():
        if isinstance(i_key,dict) and n > 0:
            resault = seach(i_key,word,n - 1)
            if resault:
                break
    else:
        resault = False
    return resault



string = input('Введите что ищем: ')
option = input('Вы хотите ограничить поиск? Y/N ').lower()
if option == 'y':
    N = int(input('Введите число: '))
else:
    N = 10000
answe = seach(site,string,N)
if answe:
    print(answe)
else:
    print('Ненайденно')

