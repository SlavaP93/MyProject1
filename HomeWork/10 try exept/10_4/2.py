import random

errors = [ArithmeticError, AssertionError, AttributeError,ValueError,BaseException,BufferError,NameError,NotADirectoryError]
r = 0
with open('out.txt','w') as file:
    try:
        while r <= 777:
                n = int(input())
                r += n
                if random.choices((0, 1), (1-1/13, 1/13))[0]:
                    raise random.choice(errors)('Случайная ошибка')
        print("Вы вышли из цикла!", n, file=file)
    finally:
        for line in file:
            print(line)
