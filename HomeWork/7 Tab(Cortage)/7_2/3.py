import random

def change(nums, rand):
    index = random.randint(0, 5)
    value = random.randint(100, 1000)
    num = list(nums[:])
    num.insert(index,value)
    nums = tuple(num)
    value += rand
    return nums, value


my_nums = 1, 2, 3, 4, 5

new_nums, rand_val = change(my_nums, 0)
print(new_nums, rand_val)
new_nums,rand_val = change(new_nums,rand_val)
print(new_nums, rand_val)
