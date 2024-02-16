def cesar(slovo, k):
    alphabit = ['абвгдеёжзийклмнопрстуфхцчшщъыьэюя']
    new_slovo = ''
    new_slovo = [for litter in ]
    for ind in slovo[0]:
        if ind != ' ':
            liter = 0
            liter += alphabit[0].index(ind) + k
            if liter >= len(alphabit[0]):
                liter -= len(alphabit[0])
            new_slovo += (alphabit[0][liter])
        else:
            new_slovo += ' '

    return new_slovo

word = []
word.append(input('Введите текст: '))
N = int(input('Введите коэфициент: '))
print('Зашифрованное слово:',cesar(word,N))
