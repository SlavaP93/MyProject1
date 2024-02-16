from random import randint

def func_1(spisok):
    new_spisok = []
    for i_ind, i_num in enumerate(spisok):
        num = (spisok[i_ind - 1], i_num)
        if i_ind % 2 == 1:
            new_spisok.append(num)
    return new_spisok


def func_2(spis):
    main = [(num, num_2) for i, num in enumerate(spis[::2])
            for i_2, num_2 in enumerate(spis[1::2]) if i == i_2]
    return main


numers = [randint(0, 10) for _ in range(10)]
print(numers)


print(func_2(numers))
print(func_1(numers))
