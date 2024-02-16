count = 0
summ = 0
with open('names.txt','r',encoding='utf-8') as text:
    for i_line in text:
        count += 1
        length = len(i_line)
        if i_line.endswith('\n'):
            length -= 1
        summ += length
        try:
            if length < 3:
                raise BaseException(open('error.log','w',encoding='utf-8').write(f'ошибка в строке {count}'))
        except BaseException:
            print(f'Ошибка в строке {count}')
    print(summ)