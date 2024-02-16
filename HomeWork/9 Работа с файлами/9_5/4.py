def func_count(file):
    koef = file.readline(3)
    box_group = dict()
    for line in file:
        data = line[:len(line)-1].split(' ')
        new_name = tuple((data[1][0],data[0]))
        if data[2] > koef:
            box_group[new_name] = data[2]
    return box_group

first_tour_data = open('first_tour.txt','r')
winners = func_count(first_tour_data)
first_tour_data.close()
second = open('second_tour.txt', 'w')
second.write(str(len(winners)))
second.write('\n')
for name,score in winners.items():
    second.write('. '.join(name))
    second.write(' ')
    second.write(score)
    second.write('\n')