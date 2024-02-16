import random

N = int(input('Введите число цифр в списке: '))
numbers_chet = [random.randint(0,100) if i % 2 != 0 else 1 for i in range(N)]
print(numbers_chet)
numbers_nechet = [num % 5 for num in numbers_chet]
print(numbers_nechet)
