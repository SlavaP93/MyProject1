pack = []
decode = []
bag = 0
packs = int(input('Число сообщений: '))
for i_pack in range(packs):
    print(i_pack + 1,' Пакет')
    for bit in range(4):
        print(bit + 1,' - Номер бита: ', end='')
        num = int(input())
        pack.append(num)
    if pack.count(-1) <= 1:
        decode.extend(pack)
    else:
        print('Слишком много ошибок в сообщении')
        bag += 1
    pack =[]

print('сообщение: ',decode)
print('недоставленно пакетов: ', bag)