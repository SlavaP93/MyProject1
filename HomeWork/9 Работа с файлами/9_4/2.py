import os

def func_find(path,new_list=None):
    if new_list == None:
        new_list = []
    if os.path.exists(path):
        for i_elem in os.listdir(path):
            new_path = os.path.join(path, i_elem)
            if os.path.isdir(new_path):
                func_find(new_path,new_list)
            elif os.path.isfile(i_elem):
                new_list.append(new_path)
        return new_list


new_path_1 = os.path.abspath(os.path.join('..','..','6 Hash table(slovar)'))

list_task = func_find(new_path_1)
for _,i in enumerate(list_task):
    new_file = open(i,'r',encoding='utf-8')
    writer = open('answer.txt', 'a',encoding='utf-8')
    for i_elem in new_file:
        writer.write(str(i_elem))
    writer.write('\n')
    writer.write('*'*28)
    writer.write('\n')
    new_file.close()
    writer.close()