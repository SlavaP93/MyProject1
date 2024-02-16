zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
print(zoo)
new_zoo = input('Ввендите новое животное: ')
ind = input('За каким животным? ')
zoo.insert(zoo.index(ind) + 1, new_zoo)
print (zoo)

zoo.remove(zoo[2])
print(zoo)
print('Лев', zoo.index('lion') + 1)