class Robot:

    def __init__(self,model):
        self.model = model

    def operate(self):
        status = f'Робот {self.model} сейчас:'
        return status

class Vacuum(Robot):

    def __init__(self, model,bag=0.0):
        super().__init__(model)
        self.bag = bag

    def operate(self):
        washing = f'\nпылесосит,заполненость мешка: {self.bag}'
        return super().operate() + washing

class Warbot(Robot):

    def __init__(self, model,gun='Standart+'):
        super().__init__(model)
        self.bag = gun

    def operate(self):
        washing = f'\nЗащищаю обЬект, оружие: {self.bag}'
        return super().operate() + washing

class Warwaterbot(Warbot):

    def __init__(self, model,gun='Standart+',deep = 0):
        super().__init__(model,gun)
        self.bag = gun
        self.deep = deep

    def operate(self):
        if self.deep == 0:
            waterdeep = f'\nНе защищаю обЬект под водой, оружие: {self.bag}, глубина: {self.deep}'
            return super().operate() + waterdeep
        else:
            waterdeep = f'\nЗащищаю обЬект под водой, оружие: {self.bag}, глубина: {self.deep}метров'
            return super().operate() + waterdeep


washer1 = Vacuum('Wash23',0.5)
print(washer1.operate())
warbot_1 = Warbot('Piu-Piu','LaserGun')
print(warbot_1.operate())
waterbot_1 = Warwaterbot('XD1')
waterbot_2 = Warwaterbot('XD2','WaterGun',50)
print(waterbot_1.operate())
print(waterbot_2.operate())