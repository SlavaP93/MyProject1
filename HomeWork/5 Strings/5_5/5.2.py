text = input('Введите строку: ').split()

main_slovo = ''
main_len = 0
k = 0
for slovo in text:
    main_len = len(slovo)
    if main_len > k:
        main_slovo = slovo
        k = main_len

print(f'Самое длинное слово в тексте: {main_slovo}, количество символов:{k}')