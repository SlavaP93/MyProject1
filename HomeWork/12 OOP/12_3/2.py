class Can_fly:
    __height = 0
    __speed = 0

    def takeoff(self):
        pass

    def fly(self):
        pass

    def landing(self):
        self.__height = 0
        self.__speed = 0

    def __get_height(self):
        return self.__height

    def __get_speed(self):
        return self.__speed

    def status(self):
        return print(f'Высота: {self.__get_height()}\nСкорость: {self.__get_speed()}')


class Batterfly(Can_fly):

    def takeoff(self):
        self.__height = 1
        return print(f'Бобочка взлетела, высота: {self.__height}')


    def fly(self):
        self.__speed = 0.5
        return print(f'Бобочка взлетела, скорость: {self.__speed}')
    
    def status(self):
        super().status()


class Rocket(Can_fly):

    def takeoff(self):
        self.__height = 500
        self.__speed = 1000
        return print(f'Ракета взлетела, высота:'
                     f' {self.__height}\nСкорость: {self.__speed}')

    def landing(self):
        return self.__explode()

    def status(self):
        return print(f'Высота: {self.__height}\nСкорость: {self.__speed}')

    def __explode(self):
        self.__height = 0
        self.__speed = 0
        return print('Бабах!!!!')


batter_1 = Batterfly()
batter_1.takeoff()
batter_1.fly()


