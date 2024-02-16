def is_palindrome(list):
    revers = []
    for i_num in range(len(list) -1, -1, -1):
        revers.append(list[i_num])
    if list == revers:
        return True
    else:
        return False

N = int(input('Кол-во чисел: '))
chisla = []
for i in range(N):
    chisla.append(int(input(f'Введите число {i + 1}: ')))
print(chisla)
new_num = []
answer = []

for i_num in range(len(chisla)):
    for j_num in range(i_num, len(chisla)):
        new_num.append(chisla[j_num])
    if is_palindrome(new_num):
        for i_answer in range(0, i_num):
            answer.append(chisla[i_answer])
        answer.reverse()
        break
    new_num = []

print(answer)


