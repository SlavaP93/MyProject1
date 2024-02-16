# Класс Итератор
# class Counteriter:
#
#     def __init__(self, N):
#         self.__num = N
#         self.__count = 0
#
#     def __next__(self):
#         self.__count += 1
#         if self.__count > self.__num:
#             raise StopIteration
#         return self.__count ** 2
#
#     def __iter__(self):
#         return self
#
#
# my_iter = Counteriter(int(input('Введите число: ')))
# for i_elem in my_iter:
#     print(i_elem)
#
# Функция Генератор
# def func_quad(N):
#     for i in range(N+1):
#         yield i ** 2
#
# for i_elem in func_quad(int(input('Введите число: '))):
#     print(i_elem)

# Генераторное выражение
N = int(input('Введите число: '))
quad_num = (num ** 2 for num in range(N+1))
for i in quad_num:
    print(i)