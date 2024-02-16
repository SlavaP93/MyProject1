def cesar(slovo, k):
    alphabit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.lower()
    new_slovo = [alphabit[(alphabit.index(ind) + k) % len(alphabit)]
                 if ind in alphabit else ind for ind in slovo]
    return new_slovo

word = input('Введите слово ').lower()
N = int(input('Введите '))

print(''.join(cesar(word,N)))