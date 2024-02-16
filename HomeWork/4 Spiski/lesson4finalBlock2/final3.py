nums_list = []
N = int(input('Кол-во видеокарт: '))
for _ in range(N):
    num = int(input('Номер модели: '))
    nums_list.append(num)
maximum = nums_list[0]
new_list = []
for i in nums_list:
    if maximum < i:
        maximum = i
for i2 in nums_list:
    if i2 != maximum:
        new_list.append(i2)

print(nums_list)
print(new_list)

