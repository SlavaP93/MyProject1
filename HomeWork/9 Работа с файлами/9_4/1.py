numer = open('numbers.txt', 'r')

count = 0
for i_num in numer:
    count += int(i_num)
numer.close()
answ = open('answer.txt', 'w')
answ.write(str(count))