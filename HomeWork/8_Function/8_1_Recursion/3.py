site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

# for i in site.values():
#     print(i)
#     for j in i.values():
#         print(j)
#         for u in j.values():
#             print(u)
def seach(dicti,key):
    if key in dicti:
        return dicti[key]

    for i_key in dicti.values():
        if isinstance(i_key,dict) is True:
            resault = seach(i_key,key)
            if resault:
                break
    else:
        resault = False
    return resault



keys = input('Что ищем?: ')
value = seach(site, keys)
if value:
    print(value)
else:
    print('Такого нет')