import os
def func_find(path):
    if os.path.exists(path):
        for i_elem in os.listdir(path):
            new_path = os.path.join(path, i_elem)
            if os.path.isdir(new_path):
                func_find(new_path)
            elif os.path.isfile(i_elem):
                print('Файл:', new_path)
                print('Размер:', os.path.getsize(new_path),'bait')


func_find(os.path.abspath(os.path.join('..')))
