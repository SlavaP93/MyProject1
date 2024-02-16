def hash_func(func):
    hash_dict = {}
    def hash(num):
        if num in hash_dict:
            return hash_dict[num]
        else:
            resault = func(num)
            hash_dict[num] = resault
            print(hash_dict)
            return resault
    return hash


@hash_func
def fibonacci(num):
    if num == 2 or num == 1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)



print(fibonacci(10))
print(fibonacci(6))