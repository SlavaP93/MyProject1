a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
even = [x for x in range(a, b + 1) if x % 2 == 0]

print(f'Чётные чисела в диапозоне от {a} до {b} \n{even}')
