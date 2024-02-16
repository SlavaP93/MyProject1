import os
def func_find(path,file):
    if os.path.exists(path):
        for i_elem in os.listdir(path):
            new_path = os.path.join(path, i_elem)
            if os.path.isdir(new_path):
                func_find(new_path,file)
            elif os.path.isfile(i_elem) and i_elem == file:
                print(new_path)


path_1 = os.path.abspath(os.path.join('..','..'))
func_find(path_1,'1.py')
