import os

real_path = os.path.abspath(os.path.sep)

if os.path.exists(os.path.join(real_path,'task','group_1.txt')):
    new_real_path = os.path.join(real_path,'task','group_1.txt')

    file = open(new_real_path,'r',encoding='utf-8')
    summa = 0
    for i_line in file:
        info = i_line.split(' ')
        summa += int(info[2])
    file.close()
    file = open(new_real_path,'r',encoding='utf-8')
    diff = 0
    for i_line in file:
        info = i_line.split(' ')
        diff -= int(info[2])
    file.close()
    print('Сумма ',summa)
    print('Что вы имели под разность? ',diff)
if os.path.exists(os.path.join(real_path, 'task', 'aditional_info','group_2.txt')):
    new_real_path = os.path.join(real_path, 'task', 'aditional_info','group_2.txt')
    file_2 = open(new_real_path, 'r',encoding='utf-8')
    compose = 1
    for i_line in file_2:
        info = i_line.split(' ')
        compose *= int(info[2])
    print('произведение? WTF? ',compose)
