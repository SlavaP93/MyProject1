import random
import string
def func_dict():
    list_1 = [random.choice(string.ascii_letters) for _ in range(10)]
    print(list_1)
    dict_1 = dict()
    for ind_1, sym_1 in enumerate(list_1):
        dict_1[ind_1] = sym_1
    return  dict_1

num = int(input('Число словарей: '))

for i in range(num):
    print(func_dict())