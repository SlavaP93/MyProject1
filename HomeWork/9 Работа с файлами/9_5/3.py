import os
def func_find(path,total_path=0,total_sum=0):
    if os.path.exists(path):
        for i_elem in os.listdir(path):
            new_path = os.path.join(path, i_elem)
            if os.path.isdir(new_path):
                total_path += 1
                func_find(new_path,total_path,total_sum)
            elif os.path.isfile(i_elem):
                print('Файл:', new_path)
                print('Размер:', os.path.getsize(new_path),'bait')
                total_sum += os.path.getsize(new_path)
        print(total_sum)
        return total_path,total_sum


path_sum, size_summ = func_find(os.path.abspath(os.path.join('..','..','projektTest')))
print(os.path.abspath(os.path.join('..','..')))
print(path_sum,size_summ)