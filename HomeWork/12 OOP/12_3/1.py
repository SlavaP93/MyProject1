class Unit:
    __hp = 100

    def __init__(self,damage=0):
        self.damage = damage

    def given_damage(self):
        self.__hp = self.__hp - self.damage
        return f'у юнита осталось {self.__hp}'

class Soldgier(Unit):

    def __init__(self,damage):
        super().__init__(damage)

class Citizen(Unit):

    def __init__(self,damage):
        super().__init__(damage*2)

soldgier_1 = Soldgier(20)
print(soldgier_1.given_damage())
citizen = Citizen(20)
print(citizen.given_damage())