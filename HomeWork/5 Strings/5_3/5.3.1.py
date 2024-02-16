text = 'я устал я ухожу я не приду я устал'.split()
user_word = input('Какие слова ищем?: ').split()

words = [word for word in user_word]
numers = [str(text.count(word1)) if word1 in text else '0' for word1 in user_word]

for index in range(len(user_word)):
    resault = 'В тексте количество слов: {word} было {numer} раз'.format(
        word=words[index],
        numer=numers[index])
    print(''.join(resault))
