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

nums = get_input_parameters()
print(nums)
print(sort_list(nums))