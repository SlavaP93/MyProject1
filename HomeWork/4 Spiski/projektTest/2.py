N = int(input('Сколько чисел? '))
numers = []
for i in range(N):
    numers.append(int(input('Введите число ')))
print('Ваш список: ',numers)
k = int(input('Введите кофициент сдвига: '))
new_numers = []
for i in numers[-k:]:
    new_numers.append(i)
s = 0
while len(new_numers) != len(numers):
    new_numers.append(numers[0 + s])
    s += 1
print(new_numers)