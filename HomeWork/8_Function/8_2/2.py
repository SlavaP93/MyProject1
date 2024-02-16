x = {1,2,3}
print(type(x))
if isinstance(x, list) or isinstance(x, dict) or isinstance(x, set):
    print('Изменяемый')
else:
    print('неИзменяемый тип данных')
print(id(x))