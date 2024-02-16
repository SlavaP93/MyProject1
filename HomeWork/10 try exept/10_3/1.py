count = 0
summ = 0
try:
    text = open('names.txt', 'r')
    for i_line in text:
        count += 1
        length = len(i_line)
        if i_line.endswith('\n'):
            length -= 1
        if length < 3:
            raise BaseException(f'Имя в строке {count} слишком короткое!')
        else:
            summ += length
    text.close()
except ValueError:
    print('Слишком короткое имя')
finally:
    print(summ)