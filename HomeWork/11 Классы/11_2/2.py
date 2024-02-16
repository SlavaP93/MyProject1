class Monitor:
    monitor_name = 'Samsung'
    monitor_matrix = 'VA'
    monitor_res = 'WQHD'
    monitor_freq = 60


class Headphones:
    headphones_name = 'Sony'
    headphones_sensitivity = 108
    headphones_micro = False


monitor_1 = Monitor()
print(monitor_1.monitor_freq, '1')
monitor_2 = Monitor()
monitor_2.monitor_freq = 144
print(monitor_2.monitor_freq,'2')
monitor_3 = Monitor()
monitor_3.monitor_freq = 70
print(monitor_3.monitor_freq,'3')
monitor_4 = Monitor()
print(monitor_4.monitor_freq,'4')

headphones_1 = Headphones()
print(headphones_1.headphones_micro,'1')
headphones_2 = Headphones()
headphones_2.headphones_micro = True
print(headphones_2.headphones_micro,'2')
headphones_3 = Headphones()
headphones_3.headphones_micro = True
print(headphones_3.headphones_micro,'3')