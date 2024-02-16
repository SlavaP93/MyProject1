import os

file = 'admin.bat'

rel_path = os.path.join('Skillbox','access',file)
full_path = os.path.abspath(os.path.join('..','..','..','..','Skillbox','access',file))
print('Полный путь:',full_path)
print('Относительный путь:',rel_path)