def func_num(num, count):
    if count > num:
        quit()
    else:
        print(count)
        return func_num(num,count + 1)


number = int(input('Введите число: '))
coun = 1
func_num(number,coun)