N = int(input('Сколько пар слов?: '))
sinon_list = []

for i in range(N):
    sinon = input('Введите синонимы через - : ').lower()
    sinon_list.append(sinon.split(' - '))

sinon_dict = dict()
for i_num in range(len(sinon_list)):
    sinon_dict[sinon_list[i_num][0]] = sinon_list[i_num][1]

answer = input('Введите слово: ').lower()

for i_slovo in sinon_dict.items():
    if i_slovo[0] == answer:
        print('Синоним: ',i_slovo[1])
        break
    elif i_slovo[1] == answer:
        print('Синоним: ',i_slovo[0])
        break
else:
    print('Такого слова нет в словаре!')


