import os

def print_lst(path):
    for i_elem in os.listdir(path):
        abs_path = os.path.abspath(os.path.join('..','..','..','..','..',i_elem))
        print(abs_path)
real_path = os.path.abspath(os.path.join('..','..','..','..','..'))
print(real_path)
print_lst(real_path)