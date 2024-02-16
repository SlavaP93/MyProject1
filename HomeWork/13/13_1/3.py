from random import uniform


class RandFloat:

    def __init__(self, limit):
        self.__count = 0
        self.__limit = limit
        self.__summ = 0

    def __next__(self):
        if self.__limit > self.__count:
            self.__count += 1
            self.__summ += uniform(0.0, 1.0)
            return round(self.__summ, 3)
        else:
            raise StopIteration

    def __iter__(self):
        return self


my_iter = RandFloat(5)

for i in my_iter:
    print(i)

print('  ')
my_iter = RandFloat(7)

for i_2 in my_iter:
    print(i_2)
