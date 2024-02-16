def tpl_sort(tpl):
    tpl1 = list(tpl)
    for i in tpl1:
        if isinstance(i,int) == False:
            return tuple(tpl1)
    if len(tpl1) < 2:
        return tpl1
    else:
        pivot = tpl1[0]
        less = [i for i in tpl1[1:] if i < pivot]
        greater = [i for i in tpl1[1:] if i > pivot]
        return tpl_sort(less) + [pivot] + tpl_sort(greater)

tpl_1 = (6, 3, -1, 8, 4, 10, -5, 9, -7)
print(tuple(tpl_sort(tpl_1)))
