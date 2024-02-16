class Toyota:
    color_car = 'White'
    price_car = 1000000
    max_speed_car = 220
    speed_moment = 0

    def info(self):
        print('Цвет: {}\nСтоймость: {}\nМаксимальная скорость: {}\nТекущая скорость: {}\n'.format(
            self.color_car,
            self.price_car,
            self.max_speed_car,
            self.speed_moment
        ))

    def new_speed(self, spped):
        self.speed_moment = spped
        print(f'Текущая скорость: {self.speed_moment}')


toyata1 = Toyota()
toyata1.info()
toyata1.new_speed(155)
