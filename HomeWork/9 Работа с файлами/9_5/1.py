new_file = open('numers.txt', 'r')
count = []
for i_elem in new_file.read():
    if i_elem != ' ':
        count.append(i_elem)
summ = 0
for i in count[::2]:
    summ += int(i)
new_file.close()
answ = open('answer.txt', 'a')
answ.write(str(summ))
