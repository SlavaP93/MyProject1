class Counteriter:

    def __init__(self):
        self.__count = 0

    def __next__(self):
        self.__count += 1
        return self.__count

    def __iter__(self):
        return self


my_iter = Counteriter()
for i_elem in my_iter:
    print(i_elem)

