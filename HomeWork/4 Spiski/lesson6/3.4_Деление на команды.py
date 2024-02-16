N = int(input('Введите кол-во участников: '))
k = int(input('Сколько человек в команде?: '))
if N % k == 0:
    raw = int(N / k)
    team = 1
    participant = []
    for _ in range(1, raw + 1):
        participant.append(list(range(team, team + k)))
        team += k
    for raw1 in participant:
        for i in raw1:
            print(i, end=' ''\t')
        print()
else:
    print(f'Невозможно поделить {N} ровно на {k}')