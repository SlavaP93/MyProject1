lst = [[2,6,2],[3,7,2],[4,8,4],[5,6,7]]
print(lst)
count = len(lst)
new_lst = [j for i in lst for j in i]
print(new_lst)
revers_lst = [new_lst[:count] if i == 0 else new_lst[count*i:count+count*i] for i in range(len(lst[0]))]
print(revers_lst)