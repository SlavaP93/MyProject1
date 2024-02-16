import math
def is_pime(index):
    num = 2
    while num <= math.sqrt(index):
        if index % num == 0:
            return False
        num += 1
    return True

def crypto(string):
    new_list = []
    for ind, sym in enumerate(string):
        if is_pime(ind) is True:
            new_list.append(sym)
    return new_list

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))