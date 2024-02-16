def func():
    count = 0
    while True:
        count += 1
        yield count

for i in func():
    print(i)