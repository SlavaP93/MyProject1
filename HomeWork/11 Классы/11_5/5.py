# Elements
class Water:

    def __init__(self, elem='Вода'):
        self.elem = elem

    def __add__(self, other):
        if other == 'Воздух':
            return Shtorm
        if other == 'Огонь':
            return Stream
        if other == 'Земля':
            return Mud


class Air:

    def __init__(self, elem='Воздух'):
        self.elem = elem

    def __add__(self, other):
        if other == 'Огонь':
            return Lightning
        if other == 'Земля':
            return Dust


class Fair:

    def __init__(self, elem='Огонь'):
        self.elem = elem

    def __add__(self, other):
        if other == 'Земля':
            return Lava


class Earth:

    def __init__(self, elem='Земля'):
        self.elem = elem


# Resault
class Shtorm:
    answer = 'Сложили два элементаля и получили: Шторм!'
    print(answer)


class Stream:
    answer = 'Сложили два элементаля и получили: Пар!'
    print(answer)


class Mud:
    answer = 'Сложили два элементаля и получили: Грязь!'
    print(answer)


class Lightning:
    answer = 'Сложили два элементаля и получили: Молния!'
    print(answer)


class Dust:
    answer = 'Сложили два элементаля и получили: Пыль!'
    print(answer)


class Lava:
    answer = 'Сложили два элементаля и получили: Лава!'
    print(answer)


elem_1 = Water()
elem_2 = Air()
elem_3 = Fair()
elem_4 = Earth

resault = elem_1 + elem_2
resault_1 = elem_1 + elem_3
resault_2 = elem_1 + elem_4
resault_3 = elem_2 + elem_3
