class Person:
    __counter = 0


    def __init__(self, name, age):
        self.__setter_name(name)
        self.__setter_age(age)
        Person.__counter += 1

    def __setter_name(self,name):
        if str(name).isalpha():
            self.__name = name
        else:
            raise ValueError('В имени должны быть только буквы')

    def __setter_age(self,age):
        if isinstance(age,(int)):
            if age in range(101):
                self.__age = age
            else:
                raise ValueError('Возраст выходит из диапозона')
        else:
            raise ValueError('Значением может быть только число')

    def get_name(self):
        return self.__name


    def get_age(self):
        return self.__age

    def get_count(self):
        return self.__counter


vasya = Person('Vasya',29)
print(vasya.get_name(),vasya.get_age())
sasha = Person('Sasha',35)
print(sasha.get_name(),sasha.get_age())
print(sasha.get_count())