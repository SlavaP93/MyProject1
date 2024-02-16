n = int(input('Введите кол-во собак: '))
scores = []
for _ in range(n):
    scores.append(int(input('Введите кол-во очков: ')))
maximum = scores[0]
minimum = scores[0]
ind = -1
ind_max = 0
ind_min = 0
for i in scores:
    ind += 1
    if maximum < i:
        maximum = i
        ind_max = ind
    if minimum > i:
        minimum = i
        ind_min = ind
print(scores)
scores[ind_max] = minimum
scores[ind_min] = maximum
print(scores)


print
print