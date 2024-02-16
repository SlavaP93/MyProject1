def sort_list(original_list):
    for i in range(len(original_list)):
        for cur_elem in range(i, len(original_list)):
            if original_list[i] > original_list[cur_elem]:
                original_list[cur_elem], original_list[i] = original_list[i], original_list[cur_elem]
    return original_list

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 0,15, 6, 8, 10]

list1.extend(list2)
main_list = []
sort_list(list1)
dubl = int
for i in list1:
    if dubl != i:
        main_list.append(i)
    dubl = i
print(main_list)

