def func_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst if i < pivot]
        gress = [j for j in lst if j > pivot]
    return func_sort(less) + [pivot] + func_sort(gress)



spis = [5, 8, 9, 4, 2, 9, 1, 8]
print(func_sort(spis))