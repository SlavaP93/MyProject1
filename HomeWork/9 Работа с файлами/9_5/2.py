def revers(file):
    lst = [i for i in file]
    text = (j for j in lst[::-1])
    return text

reader = open('dzen.txt', 'r')
for i in revers(reader):
    print(i,end='')
reader.close()