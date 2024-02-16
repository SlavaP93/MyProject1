a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
kub = [x ** 3 for x in range(a, b + 1)]
kvadrat = [x ** 2 for x in range(a, b + 1)]

print(f'Куб чисел в диапозоне от {a} до {b} \n{kub}')
print(f'Квадрат чисел в диапозоне от {a} до {b} \n{kvadrat}')