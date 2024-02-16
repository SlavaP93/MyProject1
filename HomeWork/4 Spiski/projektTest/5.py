def get_input_parameters():
    list_nums = []
    n = int(input('Количество цифр в списке: '))
    for i in range(n):
        num = int(input(f'Введите {i + 1} число: '))
        list_nums.append(num)
    print('Первоначальный список: ')
    return list_nums



def sort_list(original_list):
    for i in range(len(original_list)):
        for cur_elem in range(i, len(original_list)):
            if original_list[i] > original_list[cur_elem]:
                original_list[cur_elem], original_list[i] = original_list[i], original_list[cur_elem]
    return original_list

nums = [3, 6, 7, 8, 12, 22, 56, 54, 32, 2, 4, 5]
print(nums)
even = ''
for i in nums:
    if i % 2 != 0:
        even += str(i)
k = 0
sym = list(even)
for _ in range(len(sym)):
    sym.append(int(sym[k]))
    k += 1

print(sym)


