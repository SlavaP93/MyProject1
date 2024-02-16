from random import randint


cortage_1 = tuple(randint(0,5) for _ in range(5))
cortage_2 = tuple(randint(-5,0) for _ in range(5))
cortage_3 = tuple(cortage_1[:] + cortage_2[:])
print(cortage_3)
print('Количество нулей в кортеже:',cortage_3.count(0))
