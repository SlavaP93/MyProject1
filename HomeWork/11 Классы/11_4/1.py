class Toyota:

    def __init__(self,color,price,max_speed,current_speed):
        self.color_car = color
        self.price_car = price
        self.max_speed_car = max_speed
        self.speed_moment = current_speed

    def info(self):
        print('Цвет: {}\nСтоймость: {}\nМаксимальная скорость: {}\nТекущая скорость: {}\n'.format(
            self.color_car,
            self.price_car,
            self.max_speed_car,
            self.speed_moment
        ))

toyta1 = Toyota('Red',10**6,220,0)
toyta1.info()
toyta2 = Toyota('Black',10**7,300,0)
toyta2.info()