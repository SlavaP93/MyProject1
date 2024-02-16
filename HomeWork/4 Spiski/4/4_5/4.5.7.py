nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

main_list = [list_1 for raw in nice_list for list_1 in [col for col_1 in raw for col in col_1]]

print(main_list)