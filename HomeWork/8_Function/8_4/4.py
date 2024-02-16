def sum(*args, total=0):
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        elif isinstance(arg, (list, tuple)):
            total += sum(*arg)
    return total

spis = [[1, 2, [3]], [4], 5]
print(sum(spis))