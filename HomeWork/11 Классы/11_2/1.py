import random

class Toyota:
    color_car = 'White'
    price_car = 1000000
    max_speed_car = 220
    speed_moment = 0

new_speed_1 = Toyota()
new_speed_1.max_speed_car = random.randint(0,220)
print(new_speed_1.max_speed_car)
new_speed_2 = Toyota()
new_speed_2.max_speed_car = random.randint(0,220)
print(new_speed_2.max_speed_car)
new_speed_3 = Toyota()
new_speed_3.max_speed_car = random.randint(0,220)
print(new_speed_3.max_speed_car)