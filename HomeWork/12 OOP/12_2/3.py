class  DivisionError(Exception):
    pass

lst = []
with open('Numers.txt','r') as file:
    for i in file:
        i = i.removesuffix('\n')
        lst.append(i.split(' '))


    for ind, num in enumerate(lst):
        try:
            if int(num[0]) < int(num[1]):
                raise DivisionError
            else:
                lst[ind] = round(int(num[0]) / int(num[1]),2)
        except DivisionError:
            print('Первое число меньше второго!',ind+1)
    print(lst)


